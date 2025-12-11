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
