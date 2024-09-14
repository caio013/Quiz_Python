from typing import List

class Quiz:
    __acertos: int
    __erros: int

    def __init__(self, acertos : int, erros : int):
        self.__acertos = acertos
        self.__erros = erros

    def get_erros(self):
        return self.__erros
    
    def get_acertos(self):
        return self.__acertos
    
    def calcular_pontos(self):
        return self.__acertos - self.__erros
    
    def __str__(self):
        info = f'Acertos: {self.__acertos} Erros: {self.__erros}\n'
        info += f'Total de pontos: {self.calcular_pontos()}\n'
        return info
    
class Quiz2A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - (4*self.get_erros())

class Quiz3A(Quiz):
    def calcular_pontos(self):
        return self.get_acertos() - (2*self.get_erros())

class Aluno():
    __matricula : int
    __nome : str
    __quizes : List[Quiz]

    def __init__(self, m : int, n : str,
                 kahoots : List[Quiz]):
        self.__matricula = m
        self.__nome = n
        self.__quizes = kahoots

    def __str__(self):
        info = f'Matricula: {self.__matricula}\n'
        info += f'Nome: {self.__nome}\n'
        soma = 0
        for q in self.__quizes:
            soma += q.calcular_pontos()
        info += f'Total de pontos: {soma}\n'
        return info
    
    def get_matricula(self):
        return self.__matricula
    
class Disciplina:
    __nome : str
    __professor : str
    __ano : int
    __semestre : int
    __alunos : List[Aluno]

    def __init__(self, n : str, p : str,
                 ano : int, semestre : int):
        self.__nome = n
        self.__professor = p
        self.__ano = ano 
        self.__semestre = semestre
        self.__alunos = []

    def add_aluno(self, a : Aluno):
        for aluno in self.__alunos:
            if aluno.get_matricula() == a.get_matricula():
                raise Exception("Aluno já existe!")
        self.__alunos.append(a)

    def __str__(self):
        info = f'Disciplina: {self.__nome}\n'
        info += f'Professor: {self.__professor}\n'
        info += f'{self.__semestre} / {self.__ano}\n'
        for aluno in self.__alunos:
            info += f'{aluno}'
        return info
