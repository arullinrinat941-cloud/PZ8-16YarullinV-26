# Вариант 26
#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Элементы первого файла, отсутствующие во втором:
#Элементы второго файла, отсутствующие в первом:
#Количество элементов:
#Индекс первого минимального элемента:
#Индекс последнего максимального элемента:

# Часть 1. Работа с двумя файлами чисел
# Формируем два файла с последовательностями чисел
f1 = open('nums1.txt', 'w', encoding='utf-8')
f1.write('1 2 3 4 5 6 -1 3 5')
f1.close()

f2 = open('nums2.txt', 'w', encoding='utf-8')
f2.write('3 5 7 8 9 1 3')
f2.close()

# Читаем файлы и преобразуем в списки чисел
f1 = open('nums1.txt', encoding='utf-8')
s1 = f1.read().split()
f1.close()
for i in range(len(s1)):
    s1[i] = int(s1[i])

f2 = open('nums2.txt', encoding='utf-8')
s2 = f2.read().split()
f2.close()
for i in range(len(s2)):
    s2[i] = int(s2[i])

# Элементы первого и второго файлов (в виде списков)
elements_both = s1 + s2

# Элементы первого файла, отсутствующие во втором
absent_in_s2 = []
for x in s1:
    if x not in s2 and x not in absent_in_s2:
        absent_in_s2.append(x)

# Элементы второго файла, отсутствующие в первом
absent_in_s1 = []
for x in s2:
    if x not in s1 and x not in absent_in_s1:
        absent_in_s1.append(x)

# Количество элементов (в объединении)
count_elements = len(elements_both)

# Индекс первого минимального элемента (в объединённом списке)
min_value = elements_both[0]
for x in elements_both:
    if x < min_value:
        min_value = x
index_first_min = 0
for i in range(len(elements_both)):
    if elements_both[i] == min_value:
        index_first_min = i
        break

# Индекс последнего максимального элемента (в объединённом списке)
max_value = elements_both[0]
for x in elements_both:
    if x > max_value:
        max_value = x
index_last_max = 0
for i in range(len(elements_both)):
    if elements_both[i] == max_value:
        index_last_max = i

# Записываем результирующую информацию в файл result_26.txt
fout = open('result_26.txt', 'w', encoding='utf-8')
fout.write('Элементы первого файла:\n')
fout.write(' '.join(str(x) for x in s1) + '\n')
fout.write('Элементы второго файла:\n')
fout.write(' '.join(str(x) for x in s2) + '\n')
fout.write('Элементы первого файла, отсутствующие во втором:\n')
fout.write(' '.join(str(x) for x in absent_in_s2) + '\n')
fout.write('Элементы второго файла, отсутствующие в первом:\n')
fout.write(' '.join(str(x) for x in absent_in_s1) + '\n')
fout.write('Количество элементов (в объединении): ' + str(count_elements) + '\n')
fout.write('Индекс первого минимального элемента: ' + str(index_first_min) + '\n')
fout.write('Индекс последнего максимального элемента: ' + str(index_last_max) + '\n')
fout.close()

print('Результаты части 1 записаны в result_26.txt')