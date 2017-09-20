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
    'P': ['Q', 'T', 'O'],
    'Q': ['P', 'G', 'R'],
    'R': ['Q', 'I', 'S'],
    'S': ['R', 'K', 'T'],
    'T': ['S', 'M', 'P']
}


def find_all_paths(nodes: dict, start_node: str) -> list:
    pathCount = reduce(lambda sum, value: len(value[1]) + sum, nodes.items(), 0)
    remaining_board =  deepcopy(nodes)
    exits = remaining_board.pop(start_node, None)
    if len(exits) == 0:
        return [[start_node]]
    for key in remaining_board:
        remaining_board[key] = list(filter(lambda x : x != start_node, remaining_board[key]))
    sub_paths =  list(reduce(lambda s_paths, exit: s_paths + find_all_paths(remaining_board, exit), exits, []))
    paths = list(map(lambda p:[start_node]  + p, sub_paths))
    return paths

def find_hamiltonian_paths(nodes: dict, start_node: str) -> list:
    nodeCount = len(nodes)
    all_paths = find_all_paths(nodes, start_node)
    hamiltonian_paths = list(filter(lambda p: len(p) == nodeCount, all_paths))
    return hamiltonian_paths

def find_hamiltonian_cycles(nodes:dict, start_node: str) -> list:
    endNodes = nodes[start_node]
    hamiltonian_paths = find_hamiltonian_paths(nodes, start_node)
    hamiltonian_cycles = list(filter(lambda p: p[-1] in endNodes, hamiltonian_paths))
    return hamiltonian_cycles



print(find_hamiltonian_cycles(nodes, 'A'))