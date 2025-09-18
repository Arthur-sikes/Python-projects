import tkinter as tk
from math import sin, cos, tan, exp, log, sqrt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=10, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Advanced buttons
        advanced_buttons = [
            'sin', 'cos', 'tan', 'exp',
            'log', 'sqrt', 'C', 'DEL'
        ]

        row_val = 5
        col_val = 0

        for button in advanced_buttons:
            tk.Button(self.root, text=button, width=10, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get().replace('sin', 'sin(').replace('cos', 'cos(').replace('tan', 'tan(').replace('exp', 'exp(').replace('log', 'log(').replace('sqrt', 'sqrt(') + ')')
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'C':
            self.entry.delete(0, tk.END)
        elif button == 'DEL':
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current[:-1])
        else:
            self.entry.insert(tk.END, button)

root = tk.Tk()
root.title("Advanced Calculator")
calc = Calculator(root)
root.mainloop()