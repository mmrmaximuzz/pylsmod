"""
Parsing kernel modules info from various formats
"""

from .graphs import Graph


def parse_lsmod(content: str) -> Graph:
    """
    Parse `lsmod` output and collect deps in the directed graph
    """

    # skip the first header line
    _, *mod_strings = content.splitlines()

    graph: Graph = {}
    for mod_string in mod_strings:
        elems = mod_string.split()
        if len(elems) == 4:
            users = set(elems[-1].split(","))
        else:
            users = set()

        module, *_ = elems
        graph.setdefault(module, set())
        for user in users:
            graph.setdefault(user, set()).add(module)

    return graph


def parse_proc_modules(content: str) -> Graph:
    """
    Parse /proc/modules output without `lsmod` help
    """

    graph: Graph = {}
    for line in content.splitlines():
        module, _, _, elems, *_ = line.split()
        if elems != "-":
            users = set(elems.split(",")[:-1])  # trailing comma
        else:
            users = set()

        graph.setdefault(module, set())
        for user in users:
            graph.setdefault(user, set()).add(module)

    return graph
