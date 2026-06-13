#Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
#должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента, ФИО
#мастера, вид изделия, материал, стоимость работ.

import sqlite3


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_full_name TEXT NOT NULL,
    master_full_name TEXT NOT NULL,
    product_type TEXT NOT NULL,
    material TEXT NOT NULL,
    work_cost REAL NOT NULL
)
"""
)


initial_products = [
    ("Иванов И.И.", "Петров П.П.", "Кольцо", "Золото", 5000),
    ("Сидоров С.С.", "Кузнецов А.Н.", "Серьги", "Серебро", 3000),
    ("Попов Д.С.", "Смирнова О.В.", "Цепочка", "Золото", 7000),
    ("Васильев В.А.", "Федоров М.Ю.", "Браслет", "Платина", 12000),
    ("Морозова Е.А.", "Новиков К.П.", "Кольцо", "Серебро", 4500),
    ("Кузнецов А.Н.", "Иванов И.И.", "Подвеска", "Золото", 6500),
    ("Петров П.П.", "Сидоров С.С.", "Серьги", "Платина", 9000),
    ("Смирнова О.В.", "Попов Д.С.", "Цепочка", "Серебро", 3500),
    ("Федоров М.Ю.", "Васильев В.А.", "Браслет", "Золото", 11000),
    ("Новиков К.П.", "Морозова Е.А.", "Кольцо", "Платина", 15000),
]

cursor.executemany(
    """
INSERT INTO Product (client_full_name, master_full_name, product_type, material, work_cost)
VALUES (?, ?, ?, ?, ?)
""",
    initial_products,
)

conn.commit()



def print_products(title="Текущее состояние базы данных"):
    print(f"\n{title}")
    cursor.execute("SELECT * FROM Product")
    rows = cursor.fetchall()

    print(
        f"{'ID':<3} | {'Клиент':<15} | {'Мастер':<15} | {'Изделие':<10} | {'Материал':<10} | {'Стоимость':<8}"
    )
    print("-" * 80)

    for row in rows:
        print(
            f"{row[0]:<3} | {row[1]:<15} | {row[2]:<15} | {row[3]:<10} | {row[4]:<10} | {row[5]:<8}"
        )


print_products("Исходные данные")




# 1.поиск по типу изделия
print("\nИзделия типа 'Кольцо':")
cursor.execute("SELECT * FROM Product WHERE product_type = 'Кольцо'")
print(cursor.fetchall())

# 2.поиск по материалу золото
print("\nИзделия из золота:")
cursor.execute("SELECT * FROM Product WHERE material = 'Золото'")
print(cursor.fetchall())

# 3.поиск по стоимости больше 8000
print("\nИзделия со стоимостью > 8000:")
cursor.execute("SELECT * FROM Product WHERE work_cost > 8000")
print(cursor.fetchall())



# 1.увеличить стоимость изделий из серебра
cursor.execute(
    "UPDATE Product SET work_cost = work_cost + 1000 WHERE material = 'Серебро'"
)

# 2.изменить мастера для изделий типа "Кольцо"
cursor.execute(
    "UPDATE Product SET master_full_name = 'Иванов И.И.' WHERE product_type = 'Кольцо'"
)

# 3.заменить материал платина на золото
cursor.execute(
    "UPDATE Product SET material = 'Золото' WHERE material = 'Платина'"
)

conn.commit()
print_products("После редактирования")





cursor.execute("DELETE FROM Product WHERE work_cost < 4000")


cursor.execute("DELETE FROM Product WHERE material = 'Серебро'")

#конкретное изделие
cursor.execute("DELETE FROM Product WHERE product_type = 'Браслет'")

conn.commit()
print_products("После удаления")


conn.close()