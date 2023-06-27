antigo = open('antigo.txt', 'r')
listaAntigo = []

for linha in antigo:
    print(linha)
    # listaAntigo.append(linha)

antigo.close()  

print(listaAntigo)