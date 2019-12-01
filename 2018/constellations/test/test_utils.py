from constellations.utils import mdist


def test_mdist():
    assert mdist([1,2,3], [2,2,4]) == 2
