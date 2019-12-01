from rocket.utils import *

def test_fuel_required():
    assert fuel_required(12) == 2
    assert fuel_required(14) == 2
    assert fuel_required(1969) == 654
    assert fuel_required(100756) == 33583

def test_fuel_required_recursive():
    assert fuel_required_recursive(14) == 2
    assert fuel_required_recursive(1969) == 966
    assert fuel_required_recursive(100756) == 50346
