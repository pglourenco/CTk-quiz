import customtkinter as ctk

NUM_OF_QUESTIONS = 5

window = ctk.CTk()

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

window.geometry("500x400")
window.title("ctk_basics")

progressbar = ctk.CTkProgressBar(window, width=500, height=10, determinate_speed=(1*50)/(NUM_OF_QUESTIONS))       #size = 50
progressbar.set(0)
progressbar.pack()

def step():
    progressbar.step()

button = ctk.CTkButton(window, text='Step', command=step)
button.pack(pady=20)
    

window.mainloop()