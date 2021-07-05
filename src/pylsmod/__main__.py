"""
Main module to run pylsmod as a cli program
"""

from . import dot, graph, parser


def main() -> None:
    """
    Entry point for the lsmod. By default, reads /proc/modules and creates a
    bunch of dotfiles in the current directory
    """

    with open("/proc/modules") as modfile:
        content = modfile.read()

    modules = parser.parse_proc_modules(content)
    components = graph.make_components(modules)

    for component in components:
        dotdesc = dot.to_dotfile(component)
        roots = sorted(graph.find_roots(component))
        filename = "+".join(roots) + ".dot"
        with open(filename, "w") as dotfile:
            dotfile.write(dotdesc)


if __name__ == "__main__":
    main()
