from gurobipy import *

def solve(m, L, d, l):
    # Model
    model = Model("Binpacking with makespan")

  # Decision variable x_i_j indicates whether Item i is packed into Bin j (value 1) or not (value 0).
    x = {} 
    for i in range(len(d)):
        for j in range(m):
            # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
            x[i,j] = model.addVar(vtype='c', lb=0, name="x_%s_%s" % (i,j))

    y = {}
    for j in range(m):
        y[j] = model.addVar(vtype='b', name="y_%s" % (j))



    # Update the model to make variables known. From now on, no variables should be added.
    model.update()


    for i in range(len(d)):
        model.addConstr(quicksum(x[i,j] for j in range(m)) == d[i])

    for j in range(m):
        model.addConstr(quicksum(l[i]*x[i,j] for i in range(len(d))) <= L)

    for j in range(m):
        for i in range(len(d)):
            model.addConstr(x[i,j] <= d[i]*y[j])

            #  model.addConstr(x[i,j] > 0)




    model.setObjective(quicksum(y[j] for j in range(m)),GRB.MINIMIZE)
    #  model.ModelSense = GRB.MINIMIZE



      # Solve
    model.optimize()

      # Return the model: Do not change/remove this line - it is crucial for our scoring method
    # and removal may lead to a score of 0!
    return model
