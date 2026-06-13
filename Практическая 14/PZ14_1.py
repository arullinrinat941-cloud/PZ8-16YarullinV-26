import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Зоопарк")
window.geometry("700x600")

tk.Label(
    window,
    text="Форма заявки на работу в зоопарке",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Контактная информация
contact = tk.LabelFrame(window, text="Контактная информация")
contact.pack(fill="x", padx=10, pady=5)

tk.Label(contact, text="Имя *").grid(row=0, column=0)
tk.Entry(contact).grid(row=0, column=1)

tk.Label(contact, text="Телефон").grid(row=1, column=0)
tk.Entry(contact).grid(row=1, column=1)

tk.Label(contact, text="Email *").grid(row=2, column=0)
tk.Entry(contact).grid(row=2, column=1)

# Персональная информация
personal = tk.LabelFrame(window, text="Персональная информация")
personal.pack(fill="x", padx=10, pady=5)

tk.Label(personal, text="Возраст *").grid(row=0, column=0)
tk.Entry(personal).grid(row=0, column=1)

tk.Label(personal, text="Пол").grid(row=1, column=0)

gender = ttk.Combobox(
    personal,
    values=["Женщина", "Мужчина"]
)
gender.grid(row=1, column=1)

tk.Label(personal, text="Личные качества").grid(row=2, column=0)
tk.Text(personal, width=30, height=5).grid(row=2, column=1)

# Любимые животные
animals = tk.LabelFrame(window, text="Любимые животные")
animals.pack(fill="x", padx=10, pady=5)

for animal in ["Зебра", "Кошка", "Анаконда", "Слон"]:
    tk.Checkbutton(animals, text=animal).pack(anchor="w")

tk.Button(
    window,
    text="Отправить информацию"
).pack(pady=20)

window.mainloop()