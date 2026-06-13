import re

with open("Dostoevsky.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = set(re.findall(r"Достоевск\w*", text))

print("Найденные варианты:")
print(*sorted(words), sep="\n")