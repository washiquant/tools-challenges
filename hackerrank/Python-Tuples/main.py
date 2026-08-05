if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    x = hash(integer_tuple)
    print(x)

