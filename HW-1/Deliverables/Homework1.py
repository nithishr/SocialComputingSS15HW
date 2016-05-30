import igraph
graph = igraph.Graph.Watts_Strogatz(1,100,2,0.25)
##print graph.summary()
graph.vs["betweenness"] = graph.betweenness()
graph.save('hw1.graphml')
#print graph.edge_betweenness() == graph.betweenness()
