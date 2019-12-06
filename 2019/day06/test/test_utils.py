import pytest

from day06.utils import *

@pytest.fixture
def parents(request):
    '''
          G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
    '''
    return dict(
            L='K',
            K='J',
            J='E',
            F='E',
            E='D',
            I='D',
            D='C',
            C='B',
            H='G',
            G='B',
            B='COM')

def test_path_to_node(parents):
    ans = path_to_node(parents, 'H')
    expected = ['COM', 'B', 'G', 'H']
    assert ans == expected


def test_path_to_node_2(parents):
    ans = path_to_node(parents, 'L')
    expected = ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'L']
    assert ans == expected


def test_furthest_common_index(parents):
    path1 = ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'L']
    path2 = ['COM', 'B', 'G', 'H']
    ans = furthest_common_index(path1, path2)
    expected = 1
    assert ans == expected

def test_furthest_common_index_2(parents):
    path1 = ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'L']
    path2 = ['COM', 'B', 'C', 'D']
    ans = furthest_common_index(path1, path2)
    expected = 3
    assert ans == expected

def test_furthest_common_index_3(parents):
    path1 = ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'L']
    path2 = ['BOM', 'B', 'C', 'D']
    ans = furthest_common_index(path1, path2)
    expected = -1
    assert ans == expected

def test_furthest_common_index_3(parents):
    path1 = ['COM', 'B', 'C', 'D', 'E', 'J', 'K', 'L']
    path2 = ['BOM', 'B', 'C', 'D']
    ans = furthest_common_index(path1, path2)
    expected = -1
    assert ans == expected
