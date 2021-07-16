"""
Graph operations for lsmod package
"""

from typing import Dict, List, Set


Graph = Dict[str, Set[str]]


def make_undirected(dgraph: Graph) -> Graph:
    """
    Take directed graph and return its undirected copy
    """

    ugraph: Graph = {}
    for node, neighs in dgraph.items():
        ugraph.setdefault(node, set())
        for neigh in neighs:
            ugraph.setdefault(neigh, set())
            ugraph[node].add(neigh)
            ugraph[neigh].add(node)

    return ugraph


def make_components(dgraph: Graph) -> List[Graph]:
    """
    Returns a components list from given directed graph
    """

    # make undirected copy first to traverse without pain
    ugraph = make_undirected(dgraph)

    components = []
    pending = set(ugraph)

    while pending:
        component = {}

        # choose the start node and run BFS
        start, *_ = pending
        queue = [start]
        while queue:
            node = queue.pop(0)
            pending.discard(node)
            component[node] = dgraph.get(node, set())
            for neigh in ugraph[node]:
                if neigh in pending:
                    queue.append(neigh)

        components.append(component)

    return components


def find_roots(dgraph: Graph) -> List[str]:
    """
    Returns a list of root nodes in the directed graph (if present)
    """

    return [node for node, neighs in dgraph.items() if not neighs]
