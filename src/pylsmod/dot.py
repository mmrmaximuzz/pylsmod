"""
Module for creating dot files for graphviz software
"""

from .graph import Graph


def to_dotfile(graph: Graph) -> str:
    """
    Transforms a directed graph to a dotfile
    """

    lines = []

    # prepare nodes
    for node in graph:
        lines.append(f"\t{node}")

    for node, neighs in graph.items():
        for neigh in neighs:
            lines.append(f"\t{node} -> {neigh}")

    header = "digraph A {"
    params = "\trankdir = TB"
    footer = "}"

    return "\n".join([header, params, *lines, footer])
