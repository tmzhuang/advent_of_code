from day10.utils import *
def main():
    a = get_array('input.txt')
    asteroids = get_asteroids(a)
    los = count_los(asteroids)
    print(max_los(los))

if __name__ == '__main__':
    main()
