#from __future__ import annotations

class Question:                             # 1 linha de 1 ficheiro corresponde a 1 classe Question
    def __init__(self, all: list[str]):
        self.all = all

        self.load()

    def load(self):
        self.theme = self.all[0]
        self.question = self.all[1]
        self.a1 = self.all[2]
        self.a2 = self.all[3]
        self.a3 = self.all[4]
        self.a4 = self.all[5]
        self.ca = self.all[6]
    
    def __repr__(self):
        return f'{self.theme}, {self.question}, {self.a1}, {self.a2}, {self.a3}, {self.a4}, {self.ca}'


class Questions:                # 1 ficheiro corresponde a 1 classe Questions
    def __init__(self, file):
        self.file = file
        self.all = []       #lista de todas as perguntas

        self.load()
    
    def load(self):
        f = open(self.file, 'r', encoding='utf-8-sig')
        for line in f:
            l = line.strip().split(', ')
            q = Question(l)
            self.all.append(q)
        f.close()


qs1 = Questions(rf'C:\Users\Pedro\Desktop\python 2023 telhas\tkinter\Perguntas QO I e QO II.txt')
#print(qs1.all)

q1 = qs1.all[0]
print(q1)
print(q1.theme)

q2 = qs1.all[1]
print(q2)
