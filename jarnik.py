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
parentNodes = [0 for x in nodes]

numOfNodes: int = len(nodes)

startNode:int = 1

def findMinWeightEdge(node: int, edges: list[Edge]) -> Edge:
    list.sort(edges, key=lambda x: x.w)
    for e in edges:
        if e.p1 == node or e.p2 == node:
            return e
    return None

selected: Edge = findMinWeightEdge(startNode, edgeList)
mst: list[Edge] = [selected]
edgeList.remove(selected)

i: int = 1
while i < numOfNodes - 1:
    p1, p2 = selected.p1, selected.p2
    e1:Edge = findMinWeightEdge(p1, edgeList)
    e2:Edge = findMinWeightEdge(p2, edgeList)
    
    if e1 == None and e2 == None:
        print('exit')
        i = numOfNodes
    elif e1 == None:
        selected = e2
    elif e2 == None:
        selected = e1
    else:
        selected: Edge = e1
        if e1.w > e2.w:
            selected = e2
    
    mst.append(selected)
    edgeList.remove(selected)
    i = i+1
    
print('MST - Jarnik-Prim')
for e in mst:
    print(f'{e.p1}-{e.p2}: w={e.w}')