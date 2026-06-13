#Из предложенного текстового файла (text18-26.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно заменив все знаки пунктуации на знак «/».

# Часть 2 — student-style, с fallback кодировок и заменой знаков препинания на '/'
import string

# Чтение файла с fallback на cp1251 при ошибке декодирования
try:
    fin = open('text18-26.txt', encoding='utf-8')
    text = fin.read()
    fin.close()
except (UnicodeDecodeError, FileNotFoundError):
    try:
        fin = open('text18-26.txt', encoding='cp1251')
        text = fin.read()
        fin.close()
    except FileNotFoundError:
        # Если файла нет, создаём примерный файл и читаем его
        sample = ('И вот нашли большое поле:\n'
                  'Есть разгуляться где на воле!\n'
                  'Построили редут.\n'
                  'У наших ушки на макушке!\n'
                  'Чуть утро осветило пушки\n'
                  'И леса синие верхушки —\n'
                  'Французы тут как тут.')
        fout_tmp = open('text18-26.txt', 'w', encoding='utf-8')
        fout_tmp.write(sample)
        fout_tmp.close()
        fin = open('text18-26.txt', encoding='utf-8')
        text = fin.read()
        fin.close()

# Вывод содержимого файла
print('Содержимое text18-26.txt:')
print(text)

# Считаем знаки препинания (используем базовые ASCII пунктуации и некоторые дополнительные)
punct_marks = string.punctuation + '—«»…'
punct_count = 0
for ch in text:
    if ch in punct_marks:
        punct_count += 1

print('Количество знаков препинания:', punct_count)

# Формируем новый текст, заменяя знаки препинания на '/'
new_text = ''
for ch in text:
    if ch in punct_marks:
        new_text += '/'
    else:
        new_text += ch

# Записываем результат в выходной файл
fout2 = open('text18-26_out.txt', 'w', encoding='utf-8')
fout2.write(new_text)
fout2.close()

print('Новый файл с заменёнными знаками препинания записан в text18-26_out.txt')