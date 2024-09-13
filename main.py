from quiz import *

q1 = Quiz("POO", "Caio", 10, 2)
print(f'Erros: {q1.get_erros()}\n')
print(f'Acertos: {q1.get_acertos()}\n')
print(f'Pontuação: {q1.calcular_pontos()}\n')
print(q1)