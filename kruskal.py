from graph import Edge

e1 = Edge(1,2,2)
e2 = Edge(2,3,1)
e3 = Edge(2,5,3)
e4 = Edge(2,4,5)
e5 = Edge(4,5,1)
e6 = Edge(1,6,1)
e7 = Edge(6,5,4)
# ---
# e8 = Edge(5,3,2)

edgeList: list[Edge] = [e1,e2,e3,e4,e5,e6,e7]

node1 = [x.p1 for x in edgeList]
node2 = [x.p2 for x in edgeList]
nodes = set(node1 + node2)
numOfNodes: int = len(nodes)

# sort by weights
list.sort(edgeList,key=lambda x: x.w)

# minimal spanning tree
MST: list[Edge] = []

i = 0
while i < numOfNodes - 1:
    actualEdge = edgeList[i]
    MST.append(actualEdge)
    if actualEdge.p1 in nodes:
        nodes.remove(actualEdge.p1)
    if actualEdge.p2 in nodes:
        nodes.remove(actualEdge.p2)
    i = i + 1

print('MST is ready:')
for e in MST:
    print(f'edge: {e.p1}-{e.p2}, w={e.w}')
