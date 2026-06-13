#Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 1 – 9.

#.  Известно, что X кг конфет стоит A рублей. Определить, сколько стоит
#1 кг и Y кг этих же конфет.

from tkinter import *

from tkinter import *

def calc():
    try:
        x = float(e1.get())
        a = float(e2.get())
        y = float(e3.get())

        price_1kg = a / x
        price_y = price_1kg * y

        res.delete(0, END)
        res.insert(0, str(price_1kg) + " руб за 1кг | " + str(price_y) + " руб")

    except:
        res.delete(0, END)
        res.insert(0, "Ошибка")

root = Tk()

Label(root, text="X кг").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="A рублей").pack()
e2 = Entry(root)
e2.pack()

Label(root, text="Y кг").pack()
e3 = Entry(root)
e3.pack()

Button(root, text="Считать", command=calc).pack()

res = Entry(root, width=40)
res.pack()

root.mainloop()