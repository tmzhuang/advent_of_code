import numpy as np
from rocket.utils import *
def main():
    answer = fuel_required(np.array(INPUT)).sum()
    print(f'Answer: {answer}')
    answer2 = sum(map(fuel_required_recursive, INPUT))
    print(f'Answer2: {answer2}')
    answer2_vectorized = fuel_required_vecotrized(np.array(INPUT)).sum()
    print(f'Answer2 vectorized: {answer2_vectorized}')

if __name__ == '__main__':
    main()
