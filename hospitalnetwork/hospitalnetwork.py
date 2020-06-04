from gurobi import *
import math
import extractdata


def solve(full_instance_path):

    hospitals, cities, h_coord, c_coord, costk, capk, closing_income, cities_sp = extractdata.getHospitalData(full_instance_path)

    print(hospitals)
    print(cities)
    print(h_coord)
    print(c_coord)
    print(costk)
    print(capk)
    print(closing_income)
    print(cities_sp)


    # -----------------------------------------------------------------------
    # Initiliaze model
    # -----------------------------------------------------------------------

    model = Model("Hospital NetwORk")

    # Decision variable x_i_j indicates whether city i is allocated hospital j (value 1) or not (value 0).
    outOfRange = []
    x = {}
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            dist = math.sqrt((c_coord[i][0]-h_coord[j][0])**2+(c_coord[i][1]-h_coord[j][1])**2)
            if dist > 30:
                outOfRange.append((j,i))
            else:
                x[j,i] = model.addVar(vtype='b', name="x_%s_%s" % (j,i))

    # Decision variavle a_j_k indicates wether hostpital j is built to size k (value = 1) or not (valute = 0).
    a = {}
    for j in range(len(hospitals)):
        for k in range(3):
            a[j,k] = model.addVar(vtype='b', name="a_%s_%s" % (j,k))


    print(outOfRange)
    # Update the model to make variables known. From now on, no variables should be added.
    model.update()

    # Add the linear constraints of the model.

    # -----------------------------------------------------------------------
    # Add constraints
    # -----------------------------------------------------------------------

    #Every city musst recieve service of exactly one hospital.
    for i in range(len(cities)):
        model.addConstr(quicksum(x[j,i] for j in range(len(hospitals)) if (j,i)
            not in outOfRange) == 1)

    # Hospitals of size 1 and 2 may only serve cities in a 20km radius.
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            if (j,i) not in outOfRange:
                model.addConstr(math.sqrt((c_coord[i][0]-h_coord[j][0])**2+(c_coord[i][1]-h_coord[j][1])**2)*x[j,i]
                        <= 20*quicksum(a[j,k] for k in range(0,2)))

    # Size 3 hospitals may also serve cities 30km away.
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            if (j,i) not in outOfRange:
                k = 2
                model.addConstr(math.sqrt((c_coord[i][0]-h_coord[j][0])**2+(c_coord[i][1]-h_coord[j][1])**2)*x[j,i] <= 30*a[j,k])

    # The number of cities assigned to a hospital may not exceed the capacity limit	of the hospital at its specific size
    for j in range(len(hospitals)):
        model.addConstr(quicksum(x[j,i] for i in range(len(cities)) if (j,i)
            not in outOfRange) <= quicksum(capk[k][j]*a[j,k] for k in range(3)))

    # Cities with special needs must be served by at least a size 2 hospital.
    for j in range(len(hospitals)):
        for i in cities_sp:
            if (j,i) not in outOfRange:
                model.addConstr(x[j,i]  == quicksum(a[j,k] for k in range(1,3)))

    # Hospitals may only be built once in one size or not at all
    for j in range(len(hospitals)):
        model.addConstr(quicksum(a[j,k] for k in range(3)) <= 1)


    # -----------------------------------------------------------------------
    # Set objective and solve model
    # -----------------------------------------------------------------------

    # Set function to optimize and mode to minimize
    model.setObjective((quicksum(x[j,i]*costk[k][j] for i in
        range(len(cities)) for j in range(len(hospitals)) if
        (j,i) not in outOfRange) - quicksum(x[j,i]*closing_income[j] for i in range(len(cities))for j in
            range(len(hospitals)) if (j,i) not in outOfRange)), GRB.MINIMIZE)

    model.update()
    model.write('model.lp')

    # Solve
    model.optimize()

    return model

if __name__ == "__main__":

    import sys

    path = sys.argv[1]
    if isinstance(path, str):
        solve(path)
    else:
        print("Please enter valid string.")

