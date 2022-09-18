import math
import sys

ops = "1 - Сложение\n2 - Вычитание\n3 - Умножение\n\
4 - Деление\n5 - Возведение в степень\n6 - Логарифм\n7 - Округление в большую сторону\
 до N знака после запятой\n8 - Округление в меньшую сторону до N знака после запятой\n0 - Выход"
while True:
    try:
        print(ops)
        o = float(input("Выберете операцию (1-8): "))
        if o in range (1,9):
            if o==1:
                print("--------Сложение---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = float(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                print("Сумма = ",a+b)
                input("Нажмите любую клавишу для продолжения...")
            elif o==2:
                print("--------Вычитание---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = float(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                print("Разность = ",a-b)
                input("Нажмите любую клавишу для продолжения...")
            elif o==3:
                print("--------Умножение---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = float(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                print("Произведение = ",a*b)
                input("Нажмите любую клавишу для продолжения...")
            elif o==4:
                print("--------Деление---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = float(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                print("Частное = ",a/b)
                input("Нажмите любую клавишу для продолжения...")
            elif o==5:
                print("--------Возведение в степень---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = float(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                print("Результат = ",a^b)
                input("Нажмите любую клавишу для продолжения...")
            elif o==6:
                print("--------Логарифм---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = float(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                print("Результат = ",math.log(a,b))
                input("Нажмите любую клавишу для продолжения...")
            elif o==7:
                print("--------Округление в большую сторону до N знака после запятой---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = int(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                if a-round(a,b)>0: a=((a*(10**b))+1)/(10**b)
                print("Результат = ",round(a,b))
                input("Нажмите любую клавишу для продолжения...")
            elif o==8:
                print("--------Округление в меньшую сторону до N знака после запятой---------")
                try:
                    a=float(input("число 1: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                try:
                    b = int(input("число 2: "))
                except ValueError:
                    print("Вы ввели не число. Повторите ввод")
                if a - round(a, b) < 0: a = ((a * (10 ** b)) - 1) / (10 ** b)
                print("Результат = ",round(a,b))
                input("Нажмите любую клавишу для продолжения...")
        elif o==0: sys.exit()
        else: print("Операция выбрана не верно. Повторите ввод")
    except ValueError:
        print("Вы ввели не число. Повторите ввод")

