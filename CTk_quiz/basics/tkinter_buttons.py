import tkinter as tk
from tkinter import messagebox

class GUI:

    def __init__(self):

        self.window = tk.Tk()

        self.window.geometry("500x500")
        self.window.title("GUI_buttons")


        self.menubar = tk.Menu(self.window)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close', command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Close Without Question', command=exit)
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Show message', command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label='File')
        self.menubar.add_cascade(menu=self.actionmenu, label='Action')
        
        self.window.config(menu=self.menubar)


        self.title = tk.Label(self.window, text='Your message:')
        self.title.pack(padx=10, pady=10)

        self.input_line = tk.Entry(self.window)
        self.input_line.bind("<KeyPress>", self.shortcut)
        self.input_line.pack(padx=10, pady=10)


        self.checkstate = tk.IntVar()

        self.check = tk.Checkbutton(self.window, text='Show Messagebox', variable=self.checkstate)
        self.check.pack(padx=10, pady=10)
        

        self.button = tk.Button(self.window, text='Show message', command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbutton = tk.Button(self.window, text='Clear', command=self.clear)
        self.clearbutton.pack(padx=10, pady=10)

        self.window.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.window.mainloop()

    def show_message(self):
        if self.checkstate.get() == 0:
            print(self.input_line.get())
        else:
            messagebox.showinfo(title='Message', message=self.input_line.get())

    def clear(self):
        self.input_line.delete(0, tk.END)

    def shortcut(self, event):
        #print(event.keysym)
        #print(event.state)
        if event.keysym=='Return':  # and event.state==4
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Do you really want to quit?'):
            self.window.destroy()
        

GUI()