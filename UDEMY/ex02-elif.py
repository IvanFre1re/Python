"""1. Crie um programa no qual um profissional de educação física possa determinar de forma mais rápida quais esportes uma pessoa tem uma boa altura para praticar.
a) Solicite sua altura
b) Conforme vai digitando, deve aparecer abaixo uma dessas frases:
   "Você pode ser piloto de corrida" (altura até 1.65)
   "Você pode ser jogador de futebol" (altura +1.65 até 1.80)
   "Você pode ser jogador de vôlei ou basquete" (altura + 1.80)

"""

print('Profissional de educação física')

x = float(input('Qual sua altura'))

if x <= 1.65:
    print('Você pode ser piloto de corrida')

elif x <= 1.80:
    
    print('Você pode ser jogador de futebol')
    
else:
    
    print('Você pode seer jogador de vôlei ou basquete')