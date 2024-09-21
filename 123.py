import tkinter as tk
from datetime import datetime

class MonthListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Перемещение месяцев")
        
        self.months = [datetime(2000, month, 1).strftime('%B') for month in range(1, 13)]
        self.current_index = 0
        
        self.month_var = tk.StringVar(master)
        self.month_var.set(self.months[self.current_index])
        
        self.month_list = tk.OptionMenu(master, self.month_var, *self.months)
        self.month_list.grid(row=0, column=0, padx=10, pady=10)
        
        self.button_up = tk.Button(master, text="Вверх", command=self.move_up)
        self.button_up.grid(row=0, column=1, padx=10, pady=10)
        
        self.button_down = tk.Button(master, text="Вниз", command=self.move_down)
        self.button_down.grid(row=0, column=2, padx=10, pady=10)
    
    def move_up(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.months) - 1
        self.month_var.set(self.months[self.current_index])
    
    def move_down(self):
        self.current_index += 1
        if self.current_index >= len(self.months):
            self.current_index = 0
        self.month_var.set(self.months[self.current_index])

def main():
    root = tk.Tk()
    app = MonthListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()