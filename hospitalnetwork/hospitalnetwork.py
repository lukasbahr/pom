from gurobi import *
import math
import extractdata


def solve(full_path_instance):
    """
    input: sys argv to csv path with hospital data
    output: model
    """

    # Get hospital data from full instance path
    hospitals, cities, h_coord, c_coord, c, b, g, citiesSpecial = extractdata.getHospitalData(full_path_instance)

    print(c)
    print(b)
    print(g)
    # -----------------------------------------------------------------------
    # Initialize model
    # -----------------------------------------------------------------------

    model = Model("Hospital NetwORk")

    # Decision variable x_i_j indicates whether a city i is allocated to a
    # hospital j (value 1) or not (value 0).
    outOfRange = []
    x = {}
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            # City and hospital pairs with range over 30km must not be
            # considered in the model
            dist = math.sqrt((c_coord[i][0]-h_coord[j][0])**2+
                    (c_coord[i][1]-h_coord[j][1])**2)
            if dist > 30:
                # Keep track of the pairs out of range
                outOfRange.append((j,i))
            elif dist <= 30:
                x[j,i] = model.addVar(vtype='b', name="x_h%s_c%s" % (j+1,i+1))

    # Decision variable y_j_k indicates whether hospital j is built of size k
    # (value = 1) or not (value = 0)
    y = {}
    for j in range(len(hospitals)):
        for k in range(3):
            y[j,k] = model.addVar(vtype='b', name="y_h%s_k%s" % (j+1,k+1))

    # Make variable known to model
    model.update()


    # -----------------------------------------------------------------------
    # Linear constraints
    # -----------------------------------------------------------------------

    #Every city musst recieve service of exactly one hospital
    for i in range(len(cities)):
        model.addConstr(quicksum(x[j,i] for j in range(len(hospitals)) if (j,i)
            not in outOfRange) == 1)

    for j in range(len(hospitals)):
        # Hospitals of size 1 and 2 may only serve cities in a radius of 20km
        # or size 3 of 30km
        for i in range(len(cities)):
            if (j,i) not in outOfRange:
                model.addConstr(math.sqrt((c_coord[i][0]-h_coord[j][0])**2+
                    (c_coord[i][1]-h_coord[j][1])**2)*x[j,i] <= 20*y[j,0] +
                     20*y[j,1] + 30*y[j,2])

        # The number of cities assigned to a hospital may not exceed the
        # capacity limit of the hospital at its specific size
        model.addConstr(quicksum(x[j,i] for i in range(len(cities)) if (j,i)
            not in outOfRange) <= quicksum(b[k][j]*y[j,k] for k in range(3)))

        # Cities with special needs must be served by at least a size 2 hospital.
        for i in citiesSpecial:
            if (j,i) not in outOfRange:
                model.addConstr(x[j,i]  == quicksum(y[j,k] for k in range(1,3)))

        # Hospitals may only be built once in one size or not at all
        model.addConstr(quicksum(y[j,k] for k in range(3)) <= 1)


    # -----------------------------------------------------------------------
    # Set objective and solve model
    # -----------------------------------------------------------------------

    # Set optimize function and model sense
    model.setObjective((quicksum(c[k][j]*y[j,k] for k in range(3) for j in
        range(len(hospitals)) ) - quicksum((1-quicksum(y[j,k] for k in
            range(3)))*g[j] for j in range(len(hospitals)))), GRB.MINIMIZE)

    model.update()
    model.write('model.lp')

    # Solve model
    model.optimize()

    return model


if __name__ == "__main__":

    import sys
    path = sys.argv[1]
    solve(path)

