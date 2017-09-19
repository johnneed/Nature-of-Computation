# Bridges of Konigsberg module
from functools import reduce


def __count_degrees(edge: tuple, vertices: dict) -> dict:
    edge1, edge2 = edge
    vertices[edge1] = vertices.get(edge1, 0) + 1
    vertices[edge2] = vertices.get(edge2, 0) + 1
    return vertices


def is_solvable(edges: list) -> bool:
    vertex_degrees = reduce((lambda vertices, edge: __count_degrees(edge, vertices)), edges, {})
    odd_count = reduce((lambda total, key: total + (0 if vertex_degrees[key] % 2 == 0 else 1)), list(vertex_degrees), 0)
    return odd_count < 3


def __count_edges(edges: list) -> int:
    count = reduce((lambda total, edge: total + 1), edges, 0)
    return count


def find_solution(edges: list) -> str:
    if not is_solvable(edges):
        return 'no solution'
    return ' --> '.join(str(x) for x in __start_paths(__permutations(edges)))


def __start_paths(edge_sets: list) -> list:
    if len(edge_sets) == 0:
        return []
    edges = edge_sets[0]
    current_vertex = edges[0][0]
    path_start = [current_vertex]
    path = __create_path(edges, path_start)
    if len(path) == len(edges) + 1:
        return path
    return __start_paths(edge_sets[1:])


def __create_path(edges: list, path: list) -> list:
    current_vertex = path[-1]
    possible_exits = list(filter(lambda edge: (edge[0] == current_vertex or edge[1] == current_vertex), edges))
    if len(possible_exits) == 0:
        return path
    my_exit = possible_exits[0]
    next_vertex = my_exit[0] if (my_exit[0] != current_vertex) else my_exit[1]
    path = path + [next_vertex]
    index = edges.index(my_exit)
    remaining_edges = edges[0:index] + edges[index + 1:]
    return path if len(remaining_edges) == 0 else __create_path(remaining_edges, path)


def __permutations(arr: list, prefix: list = None) -> list:
    def flatten(l): return [item for sublist in l for item in sublist]
    if prefix is None:
        prefix = []

    if len(arr) == 0:
        return prefix + arr

    new_stuff = [__permutations(arr[:i] + arr[i + 1:], prefix + [x]) for i, x in enumerate(arr)]
    return new_stuff if (len(arr) == 1) else flatten(new_stuff)
