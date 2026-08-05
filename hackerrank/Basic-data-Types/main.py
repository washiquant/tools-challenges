x = []
numero_de_comandos = int(input())
for i in range(numero_de_comandos):
    comando = input()
    comando = comando.lower()
    comando = comando.split()

    if comando[0] == "append" :
        primeiro_inteiro = int(comando[1])
        x.append(primeiro_inteiro)

    if comando[0] == "insert" :
        primeiro_inteiro = int(comando[1])
        segundo_inteiro = int(comando[2])
        x.insert(primeiro_inteiro,segundo_inteiro)

    if comando[0] == "remove":
        primeiro_inteiro = int(comando[1])
        x.remove(primeiro_inteiro)

    if comando[0] == "pop" :
        x.pop()

    if comando[0] == "sort" :
        x.sort()

    if comando[0] == "print" :
        print(x)

    if comando[0] == "reverse" :
        x.reverse()



