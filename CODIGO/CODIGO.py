import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CALCULADORA TK")
        self.geometry("400x500")
        self.resizable(False, False)  

        self.configure(bg="#2e2e2e")
        entry_bg = "#1e1e1e"
        entry_fg = "#ffffff"
        btn_bg = "#3c3f41"
        btn_fg = "#ffffff"

        self.result_var = tk.StringVar()

        entry = tk.Entry(
            self,
            textvariable=self.result_var,
            font=("Arial", 18),
            bd=10,
            insertwidth=4,
            width=14,
            justify='right',
            bg=entry_bg,
            fg=entry_fg,
            insertbackground=entry_fg
        )
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(
                self,
                text=button,
                command=lambda b=button: self.on_button_click(b),
                font=("Arial", 18),
                bd=1,
                width=4,
                bg=btn_bg,
                fg=btn_fg,
                activebackground="#5c5f61",
                activeforeground="#ffffff"
            ).grid(row=row_val, column=col_val, sticky='nsew', padx=2, pady=2)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
                
        tk.Button(
            self,
            text='APAGAR',
            command=self.clear_entry,
            font=("Arial", 18),
            bd=1,
            bg="#ff4c4c",
            fg="#ffffff",
            activebackground="#ff6666",
            activeforeground="#ffffff"
        ).grid(row=row_val, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(row_val + 1):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
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
