def mutate_string(string: str, position: int, character: str):
    string = string.lower()
    list_string = list(string)
    list_string[position] = character
    nova_string = "".join(map(str, list_string))

    return nova_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)