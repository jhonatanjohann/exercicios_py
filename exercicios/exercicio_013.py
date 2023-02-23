numero = input("genero (f ou m): ")
altura = float(input("altura (em metros): "))

if numero == "f":
    print("peso ideal(f): {0}".format((altura * 62.1) - 44.7))    

else :
    print("peso ideal(m): {0}".format((altura * 72.7) - 58))