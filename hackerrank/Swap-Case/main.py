def swap_case(string:str) :
    nova_string = []
    for i in string :

        if i == i.lower() :
             letra_avalida = i.upper()
             nova_string.append(letra_avalida)

        elif i == i.upper() :
            letra_avalida = i.lower()
            nova_string.append(letra_avalida)


    nova_string= "".join(nova_string)
    return nova_string

swap_case("Www.HackerRank.com")