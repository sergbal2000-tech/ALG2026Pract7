numb = [5, 2, 3, 1, 4]
a = int(input("Введите число: "))

if a in numb:
    print("Поздравляю, Вы угадали число!")
    print("Список чисел:",numb)
    print("Ваше число:",a)
else:
    print("Нет такого числа!")
    print("Список чисел:",numb)
    print("Ваше число:",a)
