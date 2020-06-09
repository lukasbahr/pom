from gurobipy import *
import math
import extractdata


def solve(full_path_instance):
    """
    input: sys argv to csv path with hospital data
    output: model
    """

    # Get hospital data from full instance path
    hospitals, cities,J, J_2, I, I_2, g, b, c, K = extractdata.getHospitalData(full_path_instance)

    #  hospitals, cities, h_coord, c_coord, c, b, g, citiesSpecial = extractdata.getHospitalData(full_path_instance)

    # -----------------------------------------------------------------------
    # Initialize model
    # -----------------------------------------------------------------------

    model = Model("Hospital NetwORk")

    # Decision variable x_i_j indicates whether a city i is allocated to a
    # hospital j (value 1) or not (value 0).
    outOfRange = []
    x = {}
    for j in J:
        for i in I:
            # City and hospital pairs with range over 30km must not be
            # considered in the model
            dist = math.sqrt( (hospitals.loc[j, ' x_coord'] - cities.loc[i, ' x_coord'])**2 + (hospitals.loc[j, ' y_coord'] - cities.loc[i, ' y_coord'])**2 )

            if dist > 30:
                # Keep track of the pairs out of range
                outOfRange.append((j,i))

            elif dist <= 30:
                x[j,i] = model.addVar(vtype='b', name="x_%s_%s" % (j,i))

    # Decision variable y_j_k indicates whether hospital j is built of size k
    # (value = 1) or not (value = 0)
    y = {}
    for j in J:
        for k in K:
            y[j,k] = model.addVar(vtype='b', name="y_%s_%s" % (j, k))

    # Make variable known to model
    model.update()


    # -----------------------------------------------------------------------
    # Linear constraints
    # -----------------------------------------------------------------------

    #Every city musst recieve service of exactly one hospital
    for i in I:
        model.addConstr(quicksum(x[j,i] for j in J if (j,i)
            not in outOfRange) == 1)

    for j in J:
        # Hospitals of size 1 and 2 may only serve cities in a radius of 20km
        # or size 3 of 30km
        for i in I:
            if (j,i) not in outOfRange:
                model.addConstr(math.sqrt( (hospitals.loc[j, ' x_coord'] -
                    cities.loc[i, ' x_coord'])**2 + (hospitals.loc[j, ' y_coord'] -
                        cities.loc[i, ' y_coord'])**2)*x[j,i] <= 20*y[j,1] + 20*y[j,2] + 30*y[j,3])

        # The number of cities assigned to a hospital may not exceed the
        # capacity limit of the hospital at its specific size
        model.addConstr(quicksum(x[j,i] for i in I if (j,i)
            not in outOfRange) <= quicksum(b[k,j]*y[j,k] for k in K))

        # Cities with special needs must be served by at least a size 2 hospital.
        for i in I_2:
            if (j,i) not in outOfRange:
                model.addConstr(x[j,i]  <= quicksum(y[j,k] for k in range(2,4)))

        # Hospitals may only be built once in one size or not at all
        model.addConstr(quicksum(y[j,k] for k in K) <= 1)


    # -----------------------------------------------------------------------
    # Set objective and solve model
    # -----------------------------------------------------------------------

    # Set optimize function and model sense
    model.setObjective((quicksum(c[k,j]*y[j,k] for k in K for j in J ) -
        quicksum((1-quicksum(y[j,k] for k in K)) * g[j] for j in J_2)), GRB.MINIMIZE)

    model.update()
    model.write('model.lp')

    # Solve model
    model.optimize()

    return model


if __name__ == "__main__":

    import sys
    path = sys.argv[1]
    solve(path)

