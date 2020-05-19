import matplotlib.pyplot as plt
from networkx import nx

def solve(a, p, b):

    nitems = len(p)
    items = range(nitems)


    vertices = [[i, j] for i in range(b) for j in items]  # Vertices are named (i,j), see lecture

    k = 0
    for vertice in vertices:
        vertice.append(k)
        k += 1


    G  = nx.DiGraph()

    arcs = []  # List of tuples, i.e. [((i,j), (k,l),w), ((k,l), (u,v),0)]
    for i,j,x_1 in vertices:
        for k,l, x_2 in vertices:
            if (i == k and j == l):
                continue
            elif (i == k and l - j == 1):
                arcs.append((x_1,x_2,0))

                G.add_edge(x_1, x_2, weight=0)
            elif (i-k == -1 and j == l):
                arcs.append((x_1,x_2,1))
                G.add_edge(x_1, x_2, weight=1)




    #  print(arcs)
    #  G.add_nodes_from([0, 1, 2, 3, 4])
    #  G.add_weighted_edges_from([(1,2,3),(1,3,2)])

    #  G.add_edge('a', 'b', weight=0.6)
    #  G.add_edge('a', 'c', weight=0.2)
    #  G.add_edge('c', 'd', weight=0.1)
    #  G.add_edge('c', 'e', weight=0.7)
    #  G.add_edge('c', 'f', weight=0.9)
    #  G.add_edge('a', 'd', weight=0.3)

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

    #  pos = nx.spring_layout(G)  # positions for all nodes
    pos = nx.random_layout(G)
    
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=200)
    
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge,
                           width=1)
    nx.draw_networkx_edges(G, pos, edgelist=esmall,
                           width=1, alpha=0.5, edge_color='b', style='dashed')
    
    # labels
    nx.draw_networkx_labels(G, pos, font_size=3, font_family='sans-serif')

    #  G.add_nodes_from(vertices)
    #  print(G.number_of_nodes())
    #  G.add_edge(1, 2)

    # print the adjacency list
    #  for line in nx.generate_adjlist(G):
        #  print(line)
    # write edgelist to grid.edgelist
    #  nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
    # read edgelist from grid.edgelist
    #  H = nx.read_edgelist(path="grid.edgelist", delimiter=":")
    #  print(H)

    plt.axis('off')
    plt.show()
