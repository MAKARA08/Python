n = abs(int(input('Введите количество элементов: ')))
Y = input('Введите элементы списка: ').split()
A = list(map(int, Y))
x = int(input('Введите число X: '))

print(A.count(x))