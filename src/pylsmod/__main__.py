"""Main module to run pylsmod as a CLI program."""

import argparse

from . import dot, graphs, parsing


def cli_parser() -> argparse.ArgumentParser:
    """Create a CLI argument parser for the program."""
    argparser = argparse.ArgumentParser(
        prog="pylsmod",
        description="create a dot graph for your kernel modules")
    argparser.add_argument("--input", default="/proc/modules",
                           type=argparse.FileType(),
                           help="the path to file with /proc/modules content")
    return argparser


def main() -> None:
    """Entry point for pylsmod.

    By default, reads /proc/modules and creates a bunch of dotfiles in the
    current directory
    """
    args = cli_parser().parse_args()
    content = args.input.read()

    modules = parsing.parse_proc_modules(content)
    components = graphs.make_components(modules)

    for component in components:
        dotdesc = dot.to_dotfile(component)
        roots = sorted(graphs.find_roots(component))
        filename = "+".join(roots) + ".dot"
        with open(filename, "w") as dotfile:
            dotfile.write(dotdesc)


if __name__ == "__main__":
    main()
