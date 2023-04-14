def summa(x, y):
    x += 1
    y -= 1
    if y > 0:
        return summa(x, y)
    else:
        return x

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(summa(a, b))
