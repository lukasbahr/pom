import extractdata
from gurobipy import *
import networkx as nx




def solve(full_path_instance):

    # Get university data
    l, s, b, d, c, q, t, n, m  = extractdata.getCourseData(full_path_instance)

    # -----------------------------------------------------------------------
    # Initialize model
    # -----------------------------------------------------------------------

    model = Model("University Timetabling")


    x = {}
    z = {}
    y_assi = {}
    y_curr = {}
    y_time = {}
    y_days = {}
    T = []      # list of all timeslots for easier quicksums
    L = []      # list of all unique lecture-pairs by same teachers
    C = []      # list of all unique lecture-pairs in same curriculum

    for u in q:
        u_pair = list(itertools.combinations(q[u], 2))
        C += u_pair
    C = list(set(C))

    for a in c:
        a_pair = list(itertools.combinations(c[a], 2))
        L += a_pair
    L = list(set(L))

    for i in range(n):
        for k in l:
            z[k,i] = model.addVar(vtype = 'b', name="z_%s_%s" %(k,i))

        for j in range(m):
            T.append((i, j))

            for k in l:         # variable to assign a course k to a timeslot (i, j)
                x[k, (i, j)] = model.addVar(vtype='b', name="x_%s_(%s,%s)" % (k, i, j))

            for L_pair in L:         # variable to activate cost for assistants to give lecture
                y_assi[L_pair, (i, j)] = model.addVar(vtype=GRB.INTEGER,
                        name="y_assi_(%s_%s)_(%s,%s)" %(L_pair[0], L_pair[1], i, j))

            for C_pair in C:    # variable to activate penalty for courses of same curriculum
                y_curr[C_pair, (i, j)] = model.addVar(vtype=GRB.INTEGER,
                                           name="y_curr_(%s_%s)_(%s,%s)" % (C_pair[0], C_pair[1], i, j))

    for v in t:
        for w in t[v]:      # variable to activate penalty for using forbidden timeslots
            y_time[v,w] = model.addVar(vtype=GRB.INTEGER, name="y_time_%s_(%s)" %(v, w))

    for k in l:
        y_days[k] = model.addVar(vtype=GRB.INTEGER, name="y_days_%s" %(k))

    model.update()
    model.write('model.lp')

    for k in l:
        # reach l[k] lectures per week for course k
        model.addConstr(quicksum(x[k, (i, j)] for (i, j) in T) == l[k])

        # penalize if min. different days for lectures aren't reached
        model.addConstr(d[k]-quicksum(z[k, i] for i in range(n)) <= y_days[k])
        
        for i in range(n):
            # create a variable z[k, i] so it is 1 if a course k has lectures on day i
            model.addConstr(quicksum(x[k, (i, j)] for j in range(m)) <= m*z[k, i])
            model.addConstr(quicksum(x[k, (i, j)] for j in range(m)) >= z[k, i])

    for (i,j) in T:
        for L_pair in L:
            # variable to penalize, if lectures of courses taught by the same prof. take place at the same time
            model.addConstr(quicksum(x[k, (i, j)] for k in L_pair) <=
                    1+y_assi[L_pair, (i, j)])

        for C_pair in C:
            # variable to penalize, if lectures of courses on the same curriculum take place at the same time
            model.addConstr(quicksum(x[k, (i, j)] for k in C_pair) <=
                    1+y_curr[C_pair, (i, j)])

    for v in t:
        for w in t[v]:
            # penalize, if a certain lecture is scheduled in a certain timeslot
            model.addConstr(x[v,w] == 0+y_time[v,w])

    model.setObjective(1 * quicksum(y_assi[L_pair,(i,j)] for L_pair in L for (i,j) in T)
                       +0.1 * quicksum(y_curr[C_pair,(i,j)] for C_pair in C for (i,j) in T)
                       +10 * quicksum(x[v,w] for v in t for w in t[v])
                       +0.1 * quicksum(y_days[k] for k in l ), GRB.MINIMIZE)

    #model.update()
    #model.write('model.lp')
    #model.optimize()

    RCC_violated = True
    RCC_count = 0

    while RCC_violated:
        break_condition = []
        # Solve model initially
        model.update()
        model.optimize()
        for (i, j) in T:    # check Graph-condition for every timeslot separately

            # Graph Generation
            active_lectures = []
            G = nx.DiGraph()
            G.add_node('start')
            G.add_node('end')
            for room in b:
                G.add_edge(room, 'end', capacity=1)
            for k in s:
                G.add_edge('start', k, capacity=round(x[k, (i, j)].x))
                if round(x[k, (i, j)].x) == 1:
                    active_lectures.append(k)
                for room in b:
                    if s[k] <= b[room]:
                        G.add_edge(k, room, capacity=1)
            #print(G.number_of_nodes())
            fmax = nx.maximum_flow_value(G, 'start', 'end')

            #print(x_value)
            #print(fmax)
            if len(active_lectures) > fmax:
                RCC_count += 1
                model.addConstr(quicksum(x[k,(i,j)] for k in active_lectures) <= fmax)
                print('RCC added!')
                break_condition.append(True)
                continue

            else:
                break_condition.append(False)

        if len(set(break_condition)) < 2:
            RCC_violated = False
            print(RCC_count)


    return model

if __name__ == "__main__":

    import sys
    full_path_instance = sys.argv[1]
    solve(full_path_instance)



