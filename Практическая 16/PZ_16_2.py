#Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
#Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
#"Человек". Каждый класс должен иметь метод, который выводит информацию о
#поле объекта.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Man(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def show_gender(self):
        print(f"{self.name} — мужчина")


class Woman(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def show_gender(self):
        print(f"{self.name} — женщина")


# ввод данных
name = input("Введите имя: ")
age = int(input("Введите возраст: "))
gender = input("Введите пол (м/ж): ")

# создаём объект в зависимости от пола
if gender.lower() == "м":
    person = Man(name, age, gender)
    person.show_gender()
else:
    person = Woman(name, age, gender)
    person.show_gender()
