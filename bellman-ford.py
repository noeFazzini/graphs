''' --------- Step 1---------- '''
# This step initializes distances from the source to all vertices as infinite and distance to the source itself as 0. 
# Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.



''' --------- Step 2---------- '''
# This step calculates shortest distances. 
# Do following |V|-1 times where |V| is the number of vertices in given graph. 
# Do following for each edge u-v. If dist[v] > dist[u] + weight of edge uv, then update dist[v] to
# dist[v] = dist[u] + weight of edge uv


''' --------- Step 3 ---------- '''
# This step reports if there is a negative weight cycle in the graph. 
# Again traverse every edge and do following for each edge u-v.
# If dist[v] > dist[u] + weight of edge uv, then “Graph contains negative weight cycle” 
