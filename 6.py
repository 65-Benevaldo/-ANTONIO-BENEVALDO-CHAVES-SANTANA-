senha = input ("digite a sua senha: ")
senha_correta = "123"

while senha != senha_correta:
    print = ("senha incorreta! tente  novamente")
    senha = input ("digite a sua senha: ")

print ("acesso permitido!")

numero = int(input("digite um numero: "))

print (f"tabuada do {numero}:")

for i in range(1,  11) :
    resultado = numero * i
    print (f"{numero} X {i} = {resultado}")

    anos_experiencia = int(input("digite os anos de experiencia: "))

if anos_experiencia == 0:
     nivel = "estagiario"
elif anos_experiencia <= 3:
     nivel = "junior"
elif anos_experiencia <= 8:
     nivel = "pleno"
else:
     nivel = "senior"

print ( f"voce é um desenvolvedor no nivel: {nivel}")


anos_experiencia = int(input("digite os anos de experiencia: "))

if anos_experiencia == 0:
     nivel = "estagiario"
elif anos_experiencia <= 3:
     nivel = "junior"
elif anos_experiencia <= 8:
     nivel = "pleno"
else:
     nivel = "senior"

print ( f"voce é um desenvolvedor no nivel: {nivel}")
