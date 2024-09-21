import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

date_formats = {
    1: "ДФ = дд-ММММ-гггг",
    2: "ДЛФ = ДДВ",
    3: "ДДФ = гггг-ММ-дд",
    4: "ДМФ = ММ-дд-гггг"
}

def format_date(date, format_key):
    if format_key == 1:
        return date.strftime("%d-%B-%Y")
    elif format_key == 2:
        return date.strftime("%d.%m.%Y")
    elif format_key == 3:
        return date.strftime("%Y-%m-%d")
    elif format_key == 4:
        return date.strftime("%m-%d-%Y")

def show_selected_date():
    selected_date = date_entry.get()
    try:
        selected_date = pd.to_datetime(selected_date)
        format_key = format_selector.get()
        formatted_date = format_date(selected_date, format_key)
        messagebox.showinfo("Formatted Date", f"Formatted Date: {formatted_date}")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format")

root = tk.Tk()
root.title("Date Format Converter")

date_label = tk.Label(root, text="Enter Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=10, pady=10)

date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=10, pady=10)

format_label = tk.Label(root, text="Select Date Format:")
format_label.grid(row=1, column=0, padx=10, pady=10)

format_selector = ttk.Combobox(root, values=list(date_formats.values()))
format_selector.current(0)
format_selector.grid(row=1, column=1, padx=10, pady=10)

show_button = tk.Button(root, text="Show Formatted Date", command=show_selected_date)
show_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
