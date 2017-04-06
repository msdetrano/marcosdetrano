numero1 = float(input("Digite um numero"))
numero2 = float(input("Digite outro numero"))

categoria = int(input("1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão\n\n"))

if categoria == 1:
    operacao = (numero1+numero2)
    

elif categoria == 2:
    operacao = (numero1-numero2)

elif categoria == 3:
    operacao = (numero1*numero2)

elif categoria == 4:
    operacao = (numero1/numero2)

else: print("Voce deve digitar um numero entre 1 e 4")
print("O valor será = %6.2f"% operacao)


print("Good Bye")
