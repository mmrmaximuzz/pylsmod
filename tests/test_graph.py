"""
Test graph operations for lsmod package
"""

from pylsmod import graph


def test_make_undirected_empty():
    """
    Empty graph must remain empty
    """

    assert {} == graph.make_undirected({})


def test_make_undirected_must_copy():
    """
    Must return a new graph
    """

    arg = {}
    assert arg is not graph.make_undirected(arg)


def test_make_undirected_isolated_node():
    """
    On isolated node nothing to do
    """

    arg = {"A": set()}
    assert arg == graph.make_undirected(arg)


def test_make_undirected_isolated_nodes():
    """
    On isolated nodes nothing to do
    """

    arg = {"A": set(), "B": set()}
    assert arg == graph.make_undirected(arg)


def test_make_undirected_onehop():
    """
    A -> B becomes A -> B, B -> A
    """

    arg = {"A": {"B"}, "B": set()}
    expected = {"A": {"B"}, "B": {"A"}}
    assert expected == graph.make_undirected(arg)


def test_make_components_empty():
    """
    On empty graph must return empty components list
    """

    arg = {}
    expected = []
    assert expected == graph.make_components(arg)


def test_make_components_one_component():
    """
    Test with single linkage component
    """

    arg = {"A": {"B"}, "X": {"A"}}
    expected = [{"A": {"B"}, "X": {"A"}, "B": set()}]
    assert expected == graph.make_components(arg)


def test_make_components_multiple():
    """
    Test with several components in the graph
    """

    arg = {"Z": {"X"}, "A": {"B"}, "X": {"Y"}}
    expected = [
        {"Z": {"X"}, "X": {"Y"}, "Y": set()},
        {"A": {"B"}, "B": set()},
    ]

    components = graph.make_components(arg)

    # no another way to compare two lists of dicts
    for comp in components:
        assert comp in expected

    for comp in expected:
        assert comp in components


def test_find_roots_empty():
    """
    Must return empty root list
    """

    assert graph.find_roots({}) == []


def test_find_roots_single_edge():
    """
    On single edge graph must return one node
    """

    arg = {"A": {"B"}, "B": set()}
    assert graph.find_roots(arg) == ["B"]


def test_find_roots_no_roots():
    """
    When no root, must return empty list
    """

    arg = {"A": {"B"}, "B": {"C"}, "C": {"A"}}
    assert graph.find_roots(arg) == []
