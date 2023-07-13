antigo = open('Wasting time/testes/antigo.txt', 'r+')
listaAntigo = []

for linha in antigo:
    linha = linha.strip()
    listaAntigo.append(linha)
antigo.close()  


novo = open('Wasting time/testes/novo.txt', 'r+')
listaNovo = []

for linha in novo:
    linha = linha.strip()
    listaNovo.append(linha)
novo.close()  


terceira = []
b = 0
for i in listaAntigo:
    if listaAntigo[b] not in listaNovo:
        terceira.append(listaAntigo[b])
        b += 1

print(len(terceira))