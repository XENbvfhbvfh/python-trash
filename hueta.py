import tkinter as tk

def create_structure():
    # Создаем структуру с ключами и значениями из полей ввода
    structure = {
        "Директор": director_entry.get(),
        "ГлБухгалтер": accountant_entry.get(),
        "ГлИнженер": engineer_entry.get(),
        "Менеджер": manager_entry.get()
    }
    
    # Обходим структуру циклом и выводим сообщения
    for key, value in structure.items():
        print(f"{key}: {value}")

# Создаем графический интерфейс
root = tk.Tk()
root.title("Создание структуры")

# Поля ввода
director_label = tk.Label(root, text="Директор:")
director_label.grid(row=0, column=0)
director_entry = tk.Entry(root)
director_entry.grid(row=0, column=1)

accountant_label = tk.Label(root, text="Главный бухгалтер:")
accountant_label.grid(row=1, column=0)
accountant_entry = tk.Entry(root)
accountant_entry.grid(row=1, column=1)

engineer_label = tk.Label(root, text="Главный инженер:")
engineer_label.grid(row=2, column=0)
engineer_entry = tk.Entry(root)
engineer_entry.grid(row=2, column=1)

manager_label = tk.Label(root, text="Менеджер:")
manager_label.grid(row=3, column=0)
manager_entry = tk.Entry(root)
manager_entry.grid(row=3, column=1)

# Кнопка для создания структуры
create_button = tk.Button(root, text="Создать структуру", command=create_structure)
create_button.grid(row=4, column=0, columnspan=2)

root.mainloop()