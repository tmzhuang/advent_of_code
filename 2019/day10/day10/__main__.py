from day10.utils import *
def main():
    a = get_array('input.txt')
    asteroids = get_asteroids(a)
    count, asteroid, vectors, reduced = best_asteroid(asteroids)
    print(count)
    order_asteroids(asteroid, vectors, reduced)


if __name__ == '__main__':
    main()
