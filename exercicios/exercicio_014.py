peso = float(input("peso do peixe(kg): "))

if peso > 50 :
    maior = float( peso - 50 )
    multa = float( maior * 4 )

    print("peso maior que o estabelecido pelo regulamento: {0}kg".format(maior))
    print("total da multa: {0}$".format(multa))

else :
    print("peso dentro do regulamento: {0}kg".format(peso))