from collections import Counter

def f(x):
    cnt = Counter(x)
    return [item for item, cnt in cnt.items() if cnt > 1]

s = [1, 2, 3, 2, 4, 5, 3, 6, 7, 7, 8, 8]
a = f(s)

if a != []:
    print("Повторяющиеся элементы:",a)
else:
    print("Повторяющихся элементов нет")
