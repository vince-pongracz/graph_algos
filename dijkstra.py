
from graph import Edge, DijkstraUtil

e1 = Edge(1,2,2)
e2 = Edge(2,3,1)
e3 = Edge(2,5,3)
e4 = Edge(2,4,5)
e5 = Edge(4,5,1)
e6 = Edge(1,6,1)
e7 = Edge(6,5,4)
# ---
# e8 = Edge(1,3,1)
# e9 = Edge(3,5,1)

startnode: int = 1

edgeList: list[Edge] = [e1,e2,e3,e4,e5,e6,e7]

def initDijkstraArray(edges: list[Edge], startnode: int) -> list[DijkstraUtil]:
    node1 = [x.p1 for x in edges]
    node2 = [x.p2 for x in edges]
    nodes = set(node1 + node2)
    dijkstraArr: list[DijkstraUtil] = [DijkstraUtil(x, None, False) for x in nodes]
    
    startItemInit: DijkstraUtil = list(filter(lambda item: item.p == startnode, dijkstraArr))[0]
    startItemInit.d = 0
    [print(x) for x in dijkstraArr]
    print('---')
    return dijkstraArr

dijkstraArr = initDijkstraArray(edgeList, startnode)

def getNeigbourNodes(node: DijkstraUtil, edges: list[Edge]) -> list[Edge]:
    return list(filter(lambda item: item.p1 == node.p or item.p2 == node.p, edges))

def getPoints(edges: list[Edge]) -> set[int]:
    node1 = [x.p1 for x in edges]
    node2 = [x.p2 for x in edges]
    return set(node1 + node2)

def updateNeighbourDistances(startNode: DijkstraUtil, neighbours: list[Edge], dijkstraArr: list[DijkstraUtil]):
    points: set[int] = getPoints(neighbours)
    for n in dijkstraArr:
        if n.p == startNode.p or n.final: 
            continue
        if n.p in points:
            edgeToAdd: Edge = list(filter(lambda x: x.p1 == n.p and x.p2 == startNode.p or 
                        x.p2 == n.p and x.p1 == startNode.p, neighbours))[0]
            if n.d is None or n.d > edgeToAdd.w + startNode.d:
                n.d = edgeToAdd.w + startNode.d
                n.prevNode = startNode.p
    
def markFinalAndGetNewStartNode(dijkstraArr: list[DijkstraUtil]) -> DijkstraUtil:
    minDistNode: DijkstraUtil = min(
        list(filter(lambda x: x.final is False and x.d is not None, dijkstraArr)), key=lambda x: x.d)
    minDistNode.final = True
    return minDistNode
    
startNode: DijkstraUtil = list(filter(lambda x: x.p == startnode, dijkstraArr))[0]
i: int = 0
while i < len(dijkstraArr):
    neighbours: list[Edge] = getNeigbourNodes(startNode, edgeList)
    updateNeighbourDistances(startNode, neighbours, dijkstraArr)
    startNode = markFinalAndGetNewStartNode(dijkstraArr)
    i = i + 1
    # print(f'iter {i}:')
    # [print(x) for x in dijkstraArr]
    
print('=== RESULT: ===')
[print(x) for x in dijkstraArr]
