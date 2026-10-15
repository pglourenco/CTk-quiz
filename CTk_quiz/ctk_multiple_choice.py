import customtkinter as ctk

import tkinter as tk
from tkinter import messagebox


class RadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.radiovar = ctk.StringVar()

        rbutton_1 = ctk.CTkRadioButton(self, text='Alínea 1', variable=self.radiovar, value='1')
        rbutton_1.grid(padx=10,pady=(30,0))
        rbutton_2 = ctk.CTkRadioButton(self, text='Alínea 2', variable=self.radiovar, value='2')
        rbutton_2.grid(padx=10,pady=(30,0))
        rbutton_3 = ctk.CTkRadioButton(self, text='Alínea 3', variable=self.radiovar, value='3')
        rbutton_3.grid(padx=10,pady=(30,0))
        rbutton_4 = ctk.CTkRadioButton(self, text='Alínea 4', variable=self.radiovar, value='4')
        rbutton_4.grid(padx=10,pady=(30,0))



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.geometry("500x300")
        self.title("ctk_multiple_choice")


        self.points = 0
        self.answer = '1'        #Colocar em Question

        self.radiobutton_frame = RadiobuttonFrame(self)
        self.radiobutton_frame.pack(padx=60, pady=(10,0), fill='both', expand=True)

        submit_button = ctk.CTkButton(self, text='Submit answer', command=self.submit)
        submit_button.pack(padx=10, pady=10)

    def submit(self):
        selected_option = self.radiobutton_frame.radiovar.get()
        #print(selected_option)
        msg = ''
        if selected_option == self.answer:
            self.points += 1
            msg = 'Congratulations! You gained 1 point for guessing correctly.'
        elif selected_option == '':
            msg = 'Please pick an option.'
        else:
            msg = 'Too bad! Your answer was incorrect!'
        messagebox.showinfo(title='Submission results', message = msg + f'\nYour total number of points is {self.points}.')

def main():
    gui = App()
    gui.mainloop()

main()