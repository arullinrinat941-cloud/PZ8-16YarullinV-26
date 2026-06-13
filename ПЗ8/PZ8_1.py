# Вариант 26
#Извлеките ключи ["name", "salary"] из sample_dict.
#sample_dict = {
#"name": "Kelly",
#"age":25,
#"salary": 8000,
#"city": "New york"
#}

#Задание 1
sample_dict = {
 'name': 'Kelly',
 'age': 25,
 'salary': 8000,
 'city': 'New york'
}

print('Исходный словарь:', sample_dict)

extracted = {}
if 'name' in sample_dict:
    extracted['name'] = sample_dict['name']
if 'salary' in sample_dict:
    extracted['salary'] = sample_dict['salary']

print('Извлеченные ключи:', extracted)

