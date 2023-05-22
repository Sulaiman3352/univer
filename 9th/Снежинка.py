n = int(input("n = "))
a = []

for i in range(n):
    b = ["."] * n
    a.append(b)

for i in range(n):
    a[i][i] = "*"
    a[i][n - i - 1] = "*"

for i in range(n):
    a[i][n // 2] = "*"

for j in range(n):
    a[n // 2][j] = "*"

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j], end= " ")
    print()
