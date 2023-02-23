hora = float(input("salario por hora trabalhada: "))
mes = float(input("horas trabalhadas por mês: "))

total = float( hora * mes )
IR = float(( total  * 11 ) / 100 )
INSS = float(( total  * 8 ) / 100 )
sindicato = float(( total  * 5 ) / 100 )
liquido = float( total  - IR - INSS - sindicato )

print("SALARIO BRUTO: {0}$".format(total))
print("- IR (11%): {0}$".format(IR))
print("- INSS (8%): {0}$".format(INSS))
print("- SINDICATO (5%): {0}$".format(sindicato))
print("= SALARIO LIQUIDO: {0}$".format(liquido))