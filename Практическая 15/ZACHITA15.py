import sqlite3

# ----------------------------
# СОЗДАНИЕ БАЗЫ И ТАБЛИЦЫ
# ----------------------------
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tourists (
    client_code INTEGER PRIMARY KEY AUTOINCREMENT,
    client_surname TEXT NOT NULL,
    country_name TEXT NOT NULL,
    tour_cost REAL NOT NULL
)
""")

# ----------------------------
# ВВОД 3 ЗАПИСЕЙ
# ----------------------------
initial_tourists = [
    ("Иванов", "Турция", 50000),
    ("Петров", "Египет", 65000),
    ("Сидоров", "Италия", 90000)
]

cursor.executemany("""
INSERT INTO tourists (client_surname, country_name, tour_cost)
VALUES (?, ?, ?)
""", initial_tourists)

conn.commit()

# ----------------------------
# ВЫВОД ТАБЛИЦЫ
# ----------------------------
cursor.execute("SELECT * FROM tourists")
rows = cursor.fetchall()

print("Исходная таблица")
print(f"{'Код':<5} | {'Клиент':<10} | {'Страна':<10} | {'Стоимость':<10}")
print("-" * 45)

for row in rows:
    print(f"{row[0]:<5} | {row[1]:<10} | {row[2]:<10} | {row[3]:<10}")

# ----------------------------
# УДАЛЕНИЕ ЗАПИСИ (УСЛОВИЕ)
# ----------------------------
cursor.execute("""
DELETE FROM tourists
WHERE tour_cost > 60000
""")

conn.commit()

# ----------------------------
# ВЫВОД ПОСЛЕ УДАЛЕНИЯ
# ----------------------------
cursor.execute("SELECT * FROM tourists")
rows = cursor.fetchall()

print("\nПосле удаления записи")
print(f"{'Код':<5} | {'Клиент':<10} | {'Страна':<10} | {'Стоимость':<10}")
print("-" * 45)

for row in rows:
    print(f"{row[0]:<5} | {row[1]:<10} | {'Страна':<10} | {row[3]:<10}")

# ----------------------------
# ЗАКРЫТИЕ БАЗЫ
# ----------------------------
conn.close()