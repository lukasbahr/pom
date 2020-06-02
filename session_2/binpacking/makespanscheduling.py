from gurobipy import *

def solve(m, a, b):
    # Model
    model = Model("Binpacking with makespan")

  # Decision variable x_i_j indicates whether Item i is packed into Bin j (value 1) or not (value 0).
    x = {} 
    for i in range(len(a)): 
        for j in range(m):
            # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
            x[i,j] = model.addVar(vtype='b', name="x_%s_%s" % (i,j))

    #  # Decision variable y_j indicates whether Bin j is used (value = 1) or not (value = 0).
    #  y = {}
    #  for j in range(m):
    #      # TODO: Adjust additional attributes (lb, ub, vtype, obj). Do NOT change the name!
        #  y[j] = model.addVar(vtype='b', name="y_%s" % (j))
    C = model.addVar(vtype='c', name="makespan")



    # Update the model to make variables known. From now on, no variables should be added.
    model.update()

    # TODO: Add the linear constraints of the model. Nonlinearities in the model, e.g.,
    # multiplication of two decision variables, results in a score of 0!

    for i in range(len(a)):
        model.addConstr(quicksum(x[i,j] for j in range(m)) == 1)

    for k in range(m):
        model.addConstr(quicksum(x[j,k]*a[j] for j in range(len(a))) <= C)

    model.addConstr(C >= 0)

    # second task on makescheduling
    model.addConstr(C <= 70)


    model.setObjective(C,GRB.MINIMIZE)
    model.ModelSense = GRB.MINIMIZE



      # Solve
    model.optimize()

      # Return the model: Do not change/remove this line - it is crucial for our scoring method
    # and removal may lead to a score of 0!
    return model
