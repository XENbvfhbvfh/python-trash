import tkinter as tk
from tkinter import ttk
from datetime import date
import operator

class DateSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Date Sorter App")

        # Создание списка значений
        self.dates = ttk.Treeview(root, columns=("Date"), selectmode='browse')
        self.dates.heading("#0", text="Date")
        self.dates.heading("Date", text="Date")
        self.dates.pack(pady=10)

        # Добавление командной панели
        self.toolbar = tk.Frame(root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Кнопка сортировки по возрастанию
        self.sort_asc_button = tk.Button(self.toolbar, text="Сортировать по возрастанию", command=self.sort_asc)
        self.sort_asc_button.pack(side=tk.LEFT)

        # Кнопка сортировки по убыванию
        self.sort_desc_button = tk.Button(self.toolbar, text="Сортировать по убыванию", command=self.sort_desc)
        self.sort_desc_button.pack(side=tk.LEFT)

        # Заполнение списка значениями дат
        self.populate_dates()

    def populate_dates(self):
        # Очистка списка перед заполнением
        self.dates.delete(*self.dates.get_children())

        # Получение текущей даты
        today = date.today()

        # Добавление дат в список
        for i in range(1, 11):
            date_value = today.replace(day=i)
            self.dates.insert("", "end", text=str(i), values=(date_value))

    def sort_asc(self):
        # Сортировка списка по возрастанию
        self.dates_children = sorted(self.dates.get_children(), key=lambda x: self.dates.item(x)["values"])

        # Обновление порядка элементов в списке
        for idx, child in enumerate(self.dates_children):
            self.dates.move(child, "", idx)

    def sort_desc(self):
        # Сортировка списка по убыванию
        self.dates_children = sorted(self.dates.get_children(), key=lambda x: self.dates.item(x)["values"], reverse=True)

        # Обновление порядка элементов в списке
        for idx, child in enumerate(self.dates_children):
            self.dates.move(child, "", idx)


def main():
    root = tk.Tk()
    app = DateSorterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()