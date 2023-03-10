# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.ДОП
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n > -1:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    if n <= -1:
        return fib(n+2) - fib(n+1)

x = int(input("Введите число: "))
list = []
for x in range(-x, x+1):
    list.append(fib(x))
print(list)
