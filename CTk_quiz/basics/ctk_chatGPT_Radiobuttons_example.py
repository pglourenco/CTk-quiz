import customtkinter as ctk

class RadioExample(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CTk Radio Button Example")

        self.radio_var = ctk.IntVar()

        radio_button1 = ctk.CTkRadioButton(self, text="Option 1", variable=self.radio_var, value=1)
        radio_button1.pack(pady=5)

        radio_button2 = ctk.CTkRadioButton(self, text="Option 2", variable=self.radio_var, value=2)
        radio_button2.pack(pady=5)

        radio_button3 = ctk.CTkRadioButton(self, text="Option 3", variable=self.radio_var, value=3)
        radio_button3.pack(pady=5)

        button = ctk.CTkButton(self, text="Submit", command=self.show_selected_option)
        button.pack(pady=10)

    def show_selected_option(self):
        selected_option = self.radio_var.get()
        ctk.messagebox.showinfo("Selected Option", f"You selected option {selected_option}")

def main():
    app = RadioExample()
    app.mainloop()

if __name__ == "__main__":
    main()
