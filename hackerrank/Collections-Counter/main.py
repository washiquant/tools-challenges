def faturamento_loja():
    lucro = 0
    quantidade_de_sapatos = int(input())
    tamanhos_dos_sapatos = input()
    tamanhos_dos_sapatos = tamanhos_dos_sapatos.split()
    clientes = int(input())
    # Padronizando
    tamanhos_dos_sapatos = list(map(int, tamanhos_dos_sapatos))
    for _ in range(clientes):
        size, price = map(int, input().split())
        if size in tamanhos_dos_sapatos:
            lucro += price
            tamanhos_dos_sapatos.remove(size)
    return lucro


print(faturamento_loja())
