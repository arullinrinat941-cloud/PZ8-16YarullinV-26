#Составить генератор (yield), который выводит из строки только буквы.

def letters(text):
    for i in text:
        if i.isalpha():
            yield i

s = input("Введите строку: ")

for буква in letters(s):
    print(буква, end="")