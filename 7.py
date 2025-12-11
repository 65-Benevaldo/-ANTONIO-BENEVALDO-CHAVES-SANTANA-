horas_trabalhadas = float ( input ('digite a quantidade de hora '))
valor_hora = float (input ('digite o valor/hora: '))

if (horas_trabalhadas >= 100):
    bonus = 500.00
else:
    bonus = 0

salario = horas_trabalhadas * valor_hora + bonus

print (f"seu salario é de {salario}")

anos_experiencia = int(input("digite os anos de experiencia: "))

if anos_experiencia == 0:
    nivel = "estagiario"
elif anos_experiencia <= 3:
    nivel = "junior"
elif anos_experiencia <= 8:
    nivel = "pleno"
else:
    nivel = "senior"

print ("voce é um desenvolvedor do nivel: {nivel} ")
