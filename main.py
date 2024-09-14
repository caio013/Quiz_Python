from quiz import *

q1 = Quiz(10, 2)
q2 = Quiz2A(10, 2)
q3 = Quiz3A(10, 2)
print(f'Erros: {q1.get_erros()}\n')
print(f'Acertos: {q1.get_acertos()}\n')
print(f'Pontuação: {q1.calcular_pontos()}\n')
print(q1)
print(q2)
print(q3)

lista_q = [q1, q2, q3]
lista_q2 = [q1]
a1 = Aluno(1, "Caio", lista_q )
a2 = Aluno(2, "Cleyton", lista_q2)
a3 = Aluno(2, "Bianca", lista_q)
poo = Disciplina("POO", "Ferauche", 2024, 2)
try:
    poo.add_aluno(a1)
    poo.add_aluno(a2)
    poo.add_aluno(a3)
except Exception as e: 
    print(e)

print(poo)