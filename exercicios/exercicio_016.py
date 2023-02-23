quadrado = float(input("tamanho em metros quadrados da área a ser pintada: "))

litro = float(quadrado / 3)
tinta = float(litro / 18)
sobra = int(tinta - 0)
certo = float(tinta - sobra)
custo = float(sobra * 80)

if certo > 0 :
    if tinta > 1 :
        print("latas ultizadas: {0}".format((tinta + 1)- certo))
        print("custo: {0}$".format(custo + 80))
    
    else :
        print("latas ultizadas: 1")
        print("custo: 80.0$")

else :
    if tinta > 1 :
        print("latas ultizadas: {0}".format(tinta))
        print("custo: {0}$".format(custo))

    else :
        print("latas ultizadas: 1")
        print("custo: 80.0$")