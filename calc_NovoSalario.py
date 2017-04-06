# Calcular Ajuste salarial
sal_atual = float(input("Digite o Valor do Salario atual do Funcionario!"))
reajuste_sal = int(input("Digite o Valor do Reajuste em Porcentagem!"))
novo_Salario = sal_atual*((reajuste_sal/100)+1)
print("O valor do Salario com Reajuste é R$",novo_Salario)