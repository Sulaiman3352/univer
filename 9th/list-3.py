n = int(input("n = "))
a = []

for i in range(n):
    b = [0] * n
    a.append(b)

for i in range(n):
    a[i][i] = 1
    for j in range(i):
        a[i][j] = 2

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end= " ")
    print()


