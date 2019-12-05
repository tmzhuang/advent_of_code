from day04.utils import *
def main():
    arr = get_array(359282, 820401)
    arr = get_valid_passwords(arr)
    print(f'Answer: {arr.shape[0]}')
    arr = updated_filter_adjacent_double_rule(arr)
    print(f'Answer2: {arr.shape[0]}')

if __name__ == '__main__':
    main()
