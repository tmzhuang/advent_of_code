from day12.utils import *

def test_energy_1():
    position = get_position('input1.txt')
    position, velocity = run_simulation(position, steps=10)
    energy = calc_energy(position, velocity)
    assert energy == 179


def test_energy_2():
    position = get_position('input2.txt')
    position, velocity = run_simulation(position, steps=100)
    energy = calc_energy(position, velocity)
    assert energy == 1940
