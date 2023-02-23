quadrado = float(input("tamanho em metros quadrados da área a ser pintada: "))

litro = float(quadrado / 6)

tinta18 = float(litro / 18)
sobra = float(litro % 18)
sobra2 = float(litro % 3.6)
tinta36 = float(sobra / 3.6)

latas18 = int(tinta18 - 0)
latas36 = int(tinta36 - 0)

print("total de litros necessários:{0}".format(litro))
print("sobra dos 18l: {0}".format(sobra))
print("sobra dos 3.6l: {0}".format(sobra2))

if (tinta18 < 1 ) :
    if (tinta18 > 0) :
        print("latas 18l ultizadas: 0")
    
    else :
        print("latas 18l ultizadas: 1")


else :
    if(sobra > 0) :

        print("tinta de 18 l: {0}".format(latas18))

    else :
            print("tinta de 18l: ".format(tinta18))



if (tinta36 <= 1) :
    print("latas 3.6l ultizadas: 1")

else :
    if(sobra2 > 0) :

        print("tinta de 3.6 l: {0}".format((latas36)+ 1))

    else :
        print("tinta de 3.6 l: {0}".format(tinta36))



