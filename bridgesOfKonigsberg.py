# Bridges of Konigsberg module
from functools import reduce


def __countDegrees(edge, vertices):
    edge1, edge2 = edge
    vertices[edge1] = vertices[edge1] = vertices.get(edge1, 0) + 1
    vertices[edge2] = vertices[edge2] = vertices.get(edge2, 0) + 1
    return vertices


def isSolvable(edges):
    vertexDegrees = reduce((lambda vertices, edge: __countDegrees(edge, vertices)), edges, {})
    oddCount = reduce((lambda total, key: total + (0 if vertexDegrees[key] % 2 == 0  else 1)), list(vertexDegrees), 0)
    return oddCount < 3


def __countEdges(edges):
    count = reduce((lambda total, edge: total + 1), edges, 0)
    return count


def findSolution(edges):
    if not isSolvable(edges):
        return 'no solution'
    return __startPaths(__permutations(edges))


def __startPaths(edgeSets):
    if(len(edgeSets) == 0):
        return []
    edges = edgeSets[0]
    currentVertex = edges[0][0]
    pathStart = [currentVertex]
    path = __createPath(edges, pathStart)
    if len(path) == len(edges) + 1:
        return path
    return __startPaths(edgeSets[1:])


def __createPath(edges, path):
    currentVertex = path[-1]
    possibleExits = list(filter(lambda edge: (edge[0] == currentVertex or edge[1] == currentVertex), edges))
    if len(possibleExits) == 0:
        return path
    exit = possibleExits[0]
    nextVertex = exit[0] if (exit[0] != currentVertex) else exit[1]
    path = path + [nextVertex]
    index = edges.index(exit)
    remainingEdges = edges[0:index] + edges[index + 1:]
    return path if len(remainingEdges) == 0 else __createPath(remainingEdges, path)


def __permutations(arr, prefix=[]):
    flatten = lambda l: [item for sublist in l for item in sublist]
    if len(arr) == 0:
        return prefix + arr
    newStuff = [__permutations(arr[:i] + arr[i + 1:], prefix + [x]) for i, x in enumerate(arr)]
    return newStuff if (len(arr) == 1) else flatten(newStuff)


