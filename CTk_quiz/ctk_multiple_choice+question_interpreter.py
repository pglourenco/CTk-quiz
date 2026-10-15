import customtkinter as ctk

import tkinter as tk
from tkinter import messagebox

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

class QuestionFrame(ctk.CTkFrame):
    def __init__(self, master, questions: Questions, chosen_question: int):
        super().__init__(master)

        self.questions = questions
        self.chosen_question = chosen_question
        self.current_question = self.questions.all[self.chosen_question]

        theme_txtline = ctk.CTkLabel(self, text=self.current_question.theme)
        theme_txtline.pack()

        question_txtline = ctk.CTkLabel(self, text=self.current_question.question, font=('Arial', 18))
        question_txtline.pack()

class RadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, questions: Questions, chosen_question: int):
        super().__init__(master)

        self.questions = questions
        self.chosen_question = chosen_question
        self.current_question = self.questions.all[self.chosen_question]

        self.radiovar = ctk.StringVar()

        rbutton_1 = ctk.CTkRadioButton(self, text=self.current_question.a1, variable=self.radiovar, value=self.current_question.a1)
        rbutton_1.grid(padx=10,pady=(30,0), sticky=tk.W+tk.E)
        rbutton_2 = ctk.CTkRadioButton(self, text=self.current_question.a2, variable=self.radiovar, value=self.current_question.a2)
        rbutton_2.grid(padx=10,pady=(30,0), sticky=tk.W+tk.E)
        rbutton_3 = ctk.CTkRadioButton(self, text=self.current_question.a3, variable=self.radiovar, value=self.current_question.a3)
        rbutton_3.grid(padx=10,pady=(30,0), sticky=tk.W+tk.E)
        rbutton_4 = ctk.CTkRadioButton(self, text=self.current_question.a4, variable=self.radiovar, value=self.current_question.a4)
        rbutton_4.grid(padx=10,pady=30, sticky=tk.W+tk.E)



class App(ctk.CTk):
    def __init__(self, file_name, chosen_question: int):
        super().__init__()

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.geometry("500x400")
        self.title("ctk_multiple_choice+question_interpreter")


        self.questions = Questions(file_name)
        self.chosen_question = chosen_question

        self.points = 0


        self.question_frame = QuestionFrame(self, self.questions, self.chosen_question)
        self.question_frame.pack(padx=60, pady=10, fill='both', expand=True)

        self.radiobutton_frame = RadiobuttonFrame(self, self.questions, self.chosen_question)
        self.radiobutton_frame.pack(padx=60, pady=10, fill='both', expand=True)

        submit_button = ctk.CTkButton(self, text='Submit answer', command=self.submit)
        submit_button.pack(padx=10, pady=10)

        submit_button.destroy()

        submit_button = ctk.CTkButton(self, text='Submit answer 2', command=self.submit)
        submit_button.pack(padx=10, pady=10)


    def submit(self):
        selected_option = self.radiobutton_frame.radiovar.get()
        correct_answer = self.questions.all[self.chosen_question].ca
        #print(selected_option)
        msg = ''
        if selected_option == correct_answer:
            self.points += 1
            msg = 'Congratulations! You gained 1 point for guessing correctly.'
        elif selected_option == '':
            msg = 'Please pick an option.'
        else:
            msg = f'Too bad! Your answer was incorrect!\nThe correct answer was \"{correct_answer}\"'
        messagebox.showinfo(title='Submission results', message = msg + f'\nYour total number of points is {self.points}.')

def main():
    gui = App(rf'C:\Users\Pedro\Desktop\python 2023 telhas\tkinter\Perguntas QO I e QO II.txt', 3)
    gui.mainloop()

main()