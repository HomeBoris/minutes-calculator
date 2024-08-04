import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def add_minutes():
    try:
        time_str = entry_time.get()
        minutes_to_add = int(entry_add.get())
        
        # Преобразуем строку времени в объект времени
        time_obj = datetime.strptime(time_str, "%H:%M")
        
        # Добавляем минуты
        new_time = time_obj + timedelta(minutes=minutes_to_add)
        
        # Обновляем метку результата
        result_label.config(text=new_time.strftime("%H:%M"), fg='green')
        result_label.grid(row=5, column=1, columnspan=2, pady=10)
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное время и количество минут.")

def subtract_minutes():
    try:
        time_str = entry_time.get()
        minutes_to_subtract = int(entry_subtract.get())
        
        # Преобразуем строку времени в объект времени
        time_obj = datetime.strptime(time_str, "%H:%M")
        
        # Вычитаем минуты
        new_time = time_obj - timedelta(minutes=minutes_to_subtract)
        
        # Обновляем метку результата
        result_label.config(text=new_time.strftime("%H:%M"), fg='red')
        result_label.grid(row=5, column=1, columnspan=2, pady=10)
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное время и количество минут.")

# Создание главного окна
root = tk.Tk()
root.title("Изменение времени")

# Метка и поле ввода для времени
tk.Label(root, text="Введите время (ЧЧ:ММ):").grid(row=0, column=0, padx=10, pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=0, column=1, padx=10, pady=10)

# Метка и поле ввода для добавления минут
tk.Label(root, text="Минуты для добавления:").grid(row=1, column=0, padx=10, pady=10)
entry_add = tk.Entry(root)
entry_add.grid(row=1, column=1, padx=10, pady=10)

# Метка и поле ввода для вычитания минут
tk.Label(root, text="Минуты для вычитания:").grid(row=2, column=0, padx=10, pady=10)
entry_subtract = tk.Entry(root)
entry_subtract.grid(row=2, column=1, padx=10, pady=10)

# Кнопка для добавления минут
add_button = tk.Button(root, text="Добавить", command=add_minutes)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Кнопка для вычитания минут
subtract_button = tk.Button(root, text="Убавить", command=subtract_minutes)
subtract_button.grid(row=4, column=0, columnspan=2, pady=10)

# Поле для результата, скрытое до нажатия кнопок
result_label = tk.Label(root, text="", font=('Arial', 14))

# Запуск главного цикла
root.mainloop()
