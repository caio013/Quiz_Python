from quiz import *

q1 = Quiz("POO", "Caio", 10, 2)
q2 = Quiz2A("POO", "Julia", 10, 2)
q3 = Quiz3A("POO", "Bianca", 10, 2)
print(f'Erros: {q1.get_erros()}\n')
print(f'Acertos: {q1.get_acertos()}\n')
print(f'Pontuação: {q1.calcular_pontos()}\n')
print(q1)
print(q2)
print(q3)