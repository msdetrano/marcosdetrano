
print("Vamos Saber qual o maior time do Brasil????")
azul = 10
amarelo = 15
laranja = 20
vermelho = 30

time1 = input("Digite aqui seu time de coração:")
if time1 == ("saopaulo"):
    print(time1 + " é o maior do Brasil!")
elif time1 == ("corinthians:"):
    print(time1 + " é o maior do Brasil!")
elif time1 == ("palmeiras"):
    print(time1 + " é o maior do Brasil!")
elif time1 == ("santos"):
    print(time1 + " é o maior do Brasil!")

print("Vamos no proximo jogo do " + time1 + "???")

resposta = input("Sim ou Não??")

if resposta == ("sim"):
    print("Vamos comprar ingresso?")

elif resposta == ("nao"):
    print("Ok deixa para proxima")

respostasim = input("qual setor iremos")
if respostasim == ("azul"):
    print("O valor para 2 pessoas no setor azul é R$", azul * 2)
elif respostasim == ("amarelo"):
    print("O valoe para 2 pessoas no setor amarelo é R$", amarelo * 2)
elif respostasim == ("laranja"):
    print("O valoe para 2 pessoas no setor laranja é R$", laranja * 2)
elif respostasim == ("vermelho"):
    print("O valoe para 2 pessoas no setor vermelho é R$", vermelho * 2)


print("INGRESSOS COMPRADOS PARA O PROXIMO DOMINGO")


