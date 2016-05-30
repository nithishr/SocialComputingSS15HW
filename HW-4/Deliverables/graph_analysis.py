import igraph, pylab

g = igraph.load('social_comp.graphml')
#Graph Summary
print "Graph Summary :",igraph.summary(g)
print "Directed : ",g.is_directed() #Directed graph
print "Weighted : ",g.is_weighted() #Not weighted graph
print "Diameter: ",g.diameter() #7
print "Density: ",g.density() #0.000788246509705

#Determine the strongly connected components by clustering using strong connection
g_clusters = g.clusters(mode='strong')
#Check the cluster sizes
cluster_sizes = g_clusters.sizes()
max_cluster = max(cluster_sizes)

#Clusters of size 1
clusters_of_size_1 = cluster_sizes.count(1)
print 'No. of strongly connected components in the graph: ',len(g_clusters) #5736
print 'Length of largest strongly connected component in the graph: ',max_cluster #154
# print 'No. of strongly connected components with just single node in the graph: ',clusters_of_size_1
# print type(g.betweenness(directed=True))

#Calculate the betweenness centrality values for nodes
betweeness_centrality_values = g.betweenness(directed=True)

#Calculate the histogram for the betweenness centrality values
betweeness_centrality_values_histogram = igraph.Histogram(bin_width=10, data=betweeness_centrality_values)
# print 'Distribution of betweenness centrality values among nodes\n',betweeness_centrality_values_histogram
f=open('centrality_values.txt','w')
f.write(betweeness_centrality_values_histogram.__str__())
f.close()
print 'Mean : %f, Standard Deviation : %f, Variance : %f' %(betweeness_centrality_values_histogram.mean,
                                betweeness_centrality_values_histogram.sd, betweeness_centrality_values_histogram.var)

#Visualize the betweenness centrality values
pylab.figure()
pylab.hist(betweeness_centrality_values)
pylab.show()

#Community Infomap Clustering
community_infomap_clusters = g.community_infomap()
print 'No. of clusters in community infomap clustering: ',len(community_infomap_clusters)



