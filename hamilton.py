## Hamilton's Icosian Game
from functools import reduce
from copy import deepcopy

# Graph of the game board.
nodes = {
    'A': ['B', 'E', 'F'],
    'B': ['A', 'H', 'C'],
    'C': ['J', 'B', 'D'],
    'D': ['C', 'L', 'E'],
    'E': ['D', 'A', 'K'],
    'F': ['A', 'G', 'O'],
    'G': ['M', 'H', 'F'],
    'H': ['B', 'I', 'G'],
    'I': ['H', 'J', 'N'],
    'J': ['C', 'K', 'I'],
    'K': ['O', 'J', 'L'],
    'L': ['D', 'K', 'M'],
    'M': ['T', 'L', 'N'],
    'N': ['M', 'E', 'O'],
    'O': ['N', 'F', 'P'],
    'P': ['O', 'T', 'R'],
    'Q': ['P', 'G', 'R'],
    'R': ['Q', 'I', 'S'],
    'S': ['R', 'K', 'T'],
    'T': ['S', 'M', 'P']
}


def findHamiltonianPaths(nodes: dict, start_node: str) -> list:
    nodeCount = len(nodes)
    pathCount = reduce(lambda sum, value: len(value[1]) + sum, nodes.items(), 0)
    path = [start_node]
    remaining_board =  deepcopy(nodes)
    exits = remaining_board.pop(start_node, None)
    for key in remaining_board:
        remaining_board[key] = list(filter(lambda x : x != start_node, remaining_board[key]))
    if len(exits) == 0 :
        return path
    return path + findHamiltonianPaths(remaining_board, exits[0])



print(findHamiltonianPaths(nodes, 'A'))