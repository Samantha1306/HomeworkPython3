# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [int(i) for i in input('Введите числа через пробел: ').split()]
newlist = []
if len(list)%2 == 0:
    newlen = int(len(list)//2)
else:
    newlen = int((len(list)//2+1))
for i in range(newlen):
    newlist = [list[i]*list[len(list)-i-1] for i in range(newlen)]

print(newlist)
