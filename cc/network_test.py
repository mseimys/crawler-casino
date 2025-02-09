from cc.network import get_next_nodes, get_depth


def test_get_next_nodes():
    assert get_next_nodes("") == ["A", "B", "C", "D", "E"]
    assert get_next_nodes("C") == ["CA", "CB", "CC", "CD", "CE"]


def test_get_depth():
    assert get_depth("ABBC") == 4
