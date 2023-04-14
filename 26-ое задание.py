def power(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * power(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(power(a, b))