from gurobi import *
import math
import extractdata


def solve(full_instance_path):

    hospitals, cities, h_coord, c_coord, costk, capk, closing_income, cities_sp = extractdata.getHospitalData(full_instance_path)

    model = Model("Hospital NetwORk")

    # Decision variable x_i_j indicates whether city i is allocated hospital j (value 1) or not (value 0).
    x = {}
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            dist = math.sqrt((c_coord[i][0]-h_coord[j][0])**2+(c_coord[i][1]-h_coord[j][1])**2)
            if dist > 30:
                continue
            else:
                x[j,i] = model.addVar(vtype='b', name="x_%s_%s" % (j,i))

    # Decision variavle a_j_k indicates wether hostpital j is built to size k (value = 1) or not (valute = 0).
    a = {}
    for j in range(len(hospitals)):
        for k in range(1,4):
            a[j,k] = model.addVar(vtype='b', name="a_%s_%s" % (j,k))


    # Update the model to make variables known. From now on, no variables should be added.
    model.update()

    # Add the linear constraints of the model.

    #Every city musst recieve service of exactly one hospital.
    for i in range(len(cities)):
        model.addConstr(quicksum(x[j,i] for j in range(len(hospitals))) == 1)

    # Hospitals of size 1 and 2 may only serve cities in a 20km radius.
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            for k in range(1,4):
                model.addConstr(math.sqrt((c_coord[i][0]-h_coord[j][0])**2+(c_coord[i][1]-h_coord[j][1])**2)*x[j,i]*a[j,k] <= 20)

    # Size 3 hospitals may also serve cities 30km away.
    for j in range(len(hospitals)):
        for i in range(len(cities)):
            k = 3
            model.addConstr(math.sqrt((c_coord(i,1)-h_coord(j,1))**2+(c_coord(i,2)-h_coord(j,2))**2)*x[j,i]*a[j,k] <= 30)

    # Every hospital needs to be assigned a size of 1,2 or 3.
    for j in range(len(hospitals)):
        model.addConstr(quicksum(a[j,k] for k in range(1,4) == 1))

    # The number of cities assigned to a hospital may not exceed the capacity limit	of the hospital at its specific size
    for j in range(len(hospitals)):
        model.addConstr(quicksum(x[j,i] for i in cities) <= quicksum(capk[j,k]*a[j,k] for k in range(1,4)))

    # Cities with special needs must be served by at least a size 2 hospital.
    for i in cities_sp:
        model.addConstr(quicksum(x[j,i] * a[j,k] for j in range(len(hospitals))for k in range(2,4)) == 1)

    # Set function to optimize and mode to minimize
    model.setObjective(quicksum(x[j,i]*costk[j,k]*a[j,k] for i in
        range(len(cities))for j in range(len(hospitals)) for k in range(1,4)) -
        quicksum(x[j,i]*closing_income[j] for i in range(len(cities))for j in
            range(len(hospitals))), GRB.MINIMIZE)
    model.ModelSense = GRB.MINIMIZE



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

