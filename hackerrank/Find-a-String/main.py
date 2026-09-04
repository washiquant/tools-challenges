def count_substring(string, sub_string):
    string = string.strip()
    sub_string = sub_string.strip()
    vezes_repetidas = []
    for i in range(len(string) - len(sub_string) +1):
        if string[i:i+len(sub_string)] == sub_string :
            vezes_repetidas.append(i)
    return len(vezes_repetidas)
