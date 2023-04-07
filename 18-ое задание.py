N = abs(int(input('Введите количество элементов: ')))
Y = input('Введите элементы списка: ').split()
A = list(map(int, Y))
X = int(input('Введите число X: '))
min = abs(X - A[0])
index = 0
for i in range(1, N):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
print(A[index])