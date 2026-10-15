import customtkinter as ctk

import tkinter as tk
from tkinter import messagebox

import random

import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

class Player:                           # 1 classe Player corresponde a 1 ficheiro
    def __init__(self, name, points: int):
        self.name = name
        self.points = points

        self.file_name_first_try = os.path.join(
            PROJECT_DIR, "#players", f"#{self.name}"
        )
        self.file_name = os.path.join(PROJECT_DIR, "players", self.name)
    
    def add_points(self, amount: int):
        self.points += amount

    def check_prev_points(self) -> int:
        f = open(self.file_name, 'r', encoding='utf-8-sig')
        for line in f:
                l = line.strip().split(', ')
                prev_points = int(l[1])
                print(prev_points)
        f.close()
        print(prev_points)
        return prev_points

    def save_player_data_first_try(self):
        f = open(self.file_name_first_try, 'w', encoding='utf-8-sig')
        f.write(f'#{self.name}, {self.points}')
        f.close()
        self.save_player_data()         #é necessário criar os dois ficheiros à partida para simplificar mais à frente

    def save_player_data(self):
        f = open(self.file_name, 'w', encoding='utf-8-sig')
        f.write(f'{self.name}, {self.points}')
        f.close()

    def is_first_try(self) -> bool:
        return not os.path.exists(self.file_name_first_try)

    def __repr__(self) -> str:
        return '(' + self.name + ', ' + str(self.points) + ')'

class Players:                          # 1 classe Players corresponde à pasta players      # só será usada para a leaderboard
    def __init__(self):
        self.all_first_try = []
        self.all = []

        self.load_first_try()
        self.load()

        self.every_try = self.all_first_try + self.all
    
    def load_first_try(self):
        file_names = []
        folder_path = os.path.join(PROJECT_DIR, "#players")
        for file_name in os.listdir(folder_path):
            print(file_name)
            file_names.append(file_name)
        print(file_names)

        for file_name in file_names:
            f = open(os.path.join(folder_path, file_name), "r", encoding="utf-8-sig")
            for line in f:
                l = line.strip().split(', ')
                p = Player(l[0], l[1])
            self.all_first_try.append(p)
            f.close()

    def load(self):
        file_names = []
        folder_path = os.path.join(PROJECT_DIR, "players")
        for file_name in os.listdir(folder_path):
            print(file_name)
            file_names.append(file_name)
        print(file_names)

        for file_name in file_names:
            f = open(os.path.join(folder_path, file_name), "r", encoding="utf-8-sig")
            for line in f:
                l = line.strip().split(', ')
                p = Player(l[0], l[1])
            self.all.append(p)
            f.close()

    def find_best_player(self) -> Player:
        best_player = self.every_try[0]
        for player in self.every_try:
            if player.points > best_player.points:
                best_player = player
        print(best_player)
        return best_player

class Question:                         # 1 linha de 1 ficheiro corresponde a 1 classe Question
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

class Questions:                        # 1 ficheiro corresponde a 1 classe Questions
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


class ProgressBar(ctk.CTkProgressBar):
    def __init__(self, master, num_of_questions):
        super().__init__(master)
        
        self.num_of_questions = num_of_questions

        self.progress_bar = ctk.CTkProgressBar(self, determinate_speed=(1*50)/(num_of_questions))        #size = 50; speed = 1 question.  Regra de 3 simples:   1*50/num_of_questions
        self.progress_bar.set(0)
        self.progress_bar.grid()
    
    def step(self):
        self.progress_bar.step()

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

class LeaderboardFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=400, height=500)

        #self.title = ctk.CTkLabel(self, text='Leaderboard', font=('Arial', 20))
        #self.title.grid(row = 0, pady=10)

        self.display = ctk.CTk

        self.players = Players()
        self.players_by_order = []
        
        self.load_players_by_order()

        self.display_players()    
        
    
    def load_players_by_order(self):
        every_try_editable = self.players.every_try

        best_player = self.players.find_best_player()
        self.players_by_order.append(best_player)
        every_try_editable.remove(best_player)

        print(every_try_editable)


        for i in range(int(best_player.points)+1):
            print(i)
            for player in every_try_editable:
                print(player)
                if int(player.points) == int(best_player.points)-i:
                    print(f'yey {player}')
                    self.players_by_order.append(player)
                    print(every_try_editable) 
                

    def display_players(self):
        count = 1
        for player in self.players_by_order:
            ctk.CTkLabel(self, text = f'{count}º').grid(row=count, column = 1, padx=50,pady=(30,0), sticky=tk.W+tk.E)
            ctk.CTkLabel(self, text =player.name).grid(row=count, column = 2, padx=50,pady=(30,0), sticky=tk.W+tk.E)
            ctk.CTkLabel(self, text =player.points).grid(row=count, column = 3, padx=50,pady=(30,0), sticky=tk.W+tk.E)
            count += 1


class App(ctk.CTk):
    def __init__(self, file_name):
        super().__init__()

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.geometry("500x400")
        self.title("QUESTIONÁRIO")


        self.questions = Questions(file_name)
        self.question_number = 0
        self.available_question_list = self.create_question_list()
        self.num_of_questions = len(self.available_question_list)


        self.chosen_question = None
        self.question_frame = None
        self.radiobutton_frame = None
        self.submit_button = None

        self.welcome()

        
    def welcome(self):
        self.welcome_txtline = ctk.CTkLabel(self, text='Questionário de LQA', font=('Arial', 20))
        self.welcome_txtline.pack(pady=(10,0))
        self.author_txtline = ctk.CTkLabel(self, text='Por Pedro Lourenço', font=('Arial', 16))
        self.author_txtline.pack()

        self.insert_name = ctk.CTkEntry(self, width=200, placeholder_text='Insere o teu nome aqui')
        self.insert_name.pack(padx=10, pady=10)

        self.begin_button = ctk.CTkButton(self, text='Começar!', command=self.begin)
        self.begin_button.pack(padx=10, pady=10)

        self.show_leaderboard_button = ctk.CTkButton(self, text='Leaderboard', command=self.show_leaderboard_welcome)
        self.show_leaderboard_button.pack(pady=5)

    def begin(self):
        print(self.insert_name.get())
        name = self.insert_name.get()
        self.player = Player(name, 0)              #cria um jogador

        self.progress_bar = ProgressBar(self, self.num_of_questions)        #cria a progress bar

        self.welcome_txtline.destroy()
        self.author_txtline.destroy()
        self.insert_name.destroy()
        self.begin_button.destroy()
        self.show_leaderboard_button.destroy()

        self.show_next_question()

    def create_question_list(self):
        l = []
        for i in range(len(self.questions.all)):
            l.append(i)
        return l

    def show_next_question(self):
        if self.question_number < len(self.questions.all):
            self.chosen_question = random.choice(self.available_question_list)

            self.question_frame = QuestionFrame(self, self.questions, self.chosen_question)
            self.question_frame.pack(padx=60, pady=10, fill='both', expand=True)

            self.radiobutton_frame = RadiobuttonFrame(self, self.questions, self.chosen_question)
            self.radiobutton_frame.pack(padx=60, pady=10, fill='both', expand=True)

            self.submit_button = ctk.CTkButton(self, text='Submit answer', command=self.submit)
            self.submit_button.pack(padx=10, pady=10)
        else:
            self.game_over()

    def prep_show_next_question(self):
        self.available_question_list.remove(self.chosen_question)
        #print(self.available_question_list)
        self.question_number += 1
        self.question_frame.destroy()
        self.radiobutton_frame.destroy()
        self.submit_button.destroy()

    def submit(self):
        selected_option = self.radiobutton_frame.radiovar.get()
        correct_answer = self.questions.all[self.chosen_question].ca
        self.progress_bar.step()
        msg = ''

        if selected_option == correct_answer:
            self.player.add_points(1)
            
            msg = 'Congratulations! You gained 1 point for guessing correctly.'
            
            messagebox.showinfo(title='Submission results', message = msg + f'\nYour total number of points is {self.player.points}.')
            self.prep_show_next_question()
            self.show_next_question()

        elif selected_option == '':
            msg = 'Please pick an option.'
            
            messagebox.showinfo(title='Submission results', message = msg + f'\nYour total number of points is {self.player.points}.')

        else:
            msg = f'Too bad! Your answer was incorrect!\nThe correct answer was \"{correct_answer}\"'
            
            messagebox.showinfo(title='Submission results', message = msg + f'\nYour total number of points is {self.player.points}.')
            self.prep_show_next_question()
            self.show_next_question()

    def game_over(self):
        messagebox.showinfo(title='Game Over', message=f'Game Over! Your total number of points is {self.player.points}.')
        
        self.progress_bar.destroy()
        
        if self.player.is_first_try():
            self.player.save_player_data_first_try()
            print('is first try')
        else:
            if self.player.check_prev_points() < self.player.points:
                self.player.save_player_data()
            print('isn\'t first try')
        
        self.show_leaderboard()

    def show_leaderboard(self):
        self.leaderboard_frame = LeaderboardFrame(self)
        self.leaderboard_frame.pack()
    
        #self.play_again_button = ctk.CTkButton(self, text = "Play again!", command=self.play_again) - destruir leaderboard, resetar tudo e correr welcome(self)
        #self.play_again_button.pack(padx=10, pady=10)

    def play_again(self):
        self.leaderboard_frame.destroy()

        #RESETAR TUDO
        
        self.welcome()

    def show_leaderboard_welcome(self):
        self.welcome_txtline.destroy()
        self.author_txtline.destroy()
        self.insert_name.destroy()
        self.begin_button.destroy()
        self.show_leaderboard_button.destroy()

        self.leaderboard_frame = LeaderboardFrame(self)
        self.leaderboard_frame.pack()

        #self.back_button = ctk.CTkButton(self, text = "Back", command=self.back_to_welcome)  - destruir leaderboard e correr welcome(self)      
        #self.back_button.pack(padx=10, pady=10)

    def back_to_welcome(self):
        self.leaderboard_frame.destroy()
        self.back_button.destroy()

        self.welcome()


def main():
    gui = App(os.path.join(PROJECT_DIR, "Perguntas.txt"))
    gui.mainloop()

main()
