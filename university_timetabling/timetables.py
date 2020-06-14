import extractdata
from gurobipy import *



def solve(full_path_instance):

    # Get university data
    l, s, b, d, c, q, t, n, m  = extractdata.getCourseData(full_path_instance)

    # -----------------------------------------------------------------------
    # Initialize model
    # -----------------------------------------------------------------------

    model = Model("Hospital NetwORk")


    x = {}
    z = {}
    y_assi = {}
    y_curr = {}
    y_time = {}
    y_days = {}
    T = []

    for i in range(n):
        for k in l:
            z[k,i] = model.addVar(vtype = 'b', name="z_%s_%s" %(k,i))

        for j in range(m):
            T.append((i,j))

            for k in l:
                x[k,(i,j)] = model.addVar(vtype='b', name="x_%s_(%s,%s)" % (k,i,j))

            for a in c:
                y_assi[a,(i,j)] = model.addVar(vtype=GRB.INTEGER,
                        name="y_assi_%s_(%s,%s)" %(a,i,j))

            for u in q:
                y_curr[u,(i,j)] = model.addVar(vtype=GRB.INTEGER,
                        name="y_curr_%s_(%s,%s)" %(u,i,j))

    for v in t:
        for w in t[v]:
                y_time[v,w] = model.addVar(vtype=GRB.INTEGER,
                        name="y_curr_%s_(%s)" %(v,w))


    for k in l:
        y_days[k] = model.addVar(vtype = GRB.INTEGER, name = "y_days_%s" %(k))

    model.update()

    for k in l:
        model.addConstr(quicksum(x[k,(i,j)] for (i,j) in T) == l[k])

        model.addConstr(quicksum(d[k]-z[k,i] for i in range(n)) == y_days[k])

        for i in range(n):
            model.addConstr(quicksum(x[k,(i,j)] for j in range(m))*(1-z[k,i])
                    == 0 )

    for (i,j) in T:
        for a in c:
            model.addConstr(quicksum(x[k,(i,j)] for k in c[a]) <=
                    1+y_assi[a,(i,j)])

        for u in q:
            model.addConstr(quicksum(x[k,(i,j)] for k in q[u]) <=
                    1+y_curr[u,(i,j)])

    for v in t:
        for w in t[v]:
            model.addConstr(x[v,w]==0+y_time[v,w])


    model.write('model.lp')

    # Solve model
    model.optimize()

    return model


if __name__ == "__main__":

    import sys
    full_path_instance = sys.argv[1]
    solve(full_path_instance)



