import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CALCULADORA")
        self.geometry("400x500")

        self.result_var = tk.StringVar()

        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 18), bd=10, insertwidth=4, width=14, justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, command=lambda b=button: self.on_button_click(b), font=("Arial", 18), bd=10, width=4).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self, text='C', command=self.clear_entry, font=("Arial", 18), bd=10, width=4).grid(row=row_val, column=col_val, sticky='nsew')

        for i in range(1, 6):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Erro")
        else:
            current_value = self.result_var.get()
            new_value = current_value + str(value)
            self.result_var.set(new_value)

    def clear_entry(self):
        self.result_var.set("")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
