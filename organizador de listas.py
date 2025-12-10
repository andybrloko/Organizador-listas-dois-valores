listaN = ([])
listaV = ([])
listaNa = input("Quais nomes você deseja adicionar à lista? ").split()
listaN = listaNa
#===============================================
listaVa = input("Quais valores você deseja adicionar à lista? ").split()
listaV = listaVa
#===============================================
dados_ass = dict(zip(listaN, listaV))
if not listaN:
    print("não há nada na lista")
elif not listaV:
    print("não há nada na lista")
else:
        ordenado = sorted(dados_ass.items(), key=lambda x: x[1], reverse=True)
        print("nome                        valor")
        print ("-" * 30)
        for nome, valor in ordenado:
            print(f'{nome:<20} {valor:>10}')