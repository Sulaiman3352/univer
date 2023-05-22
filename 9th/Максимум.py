n, m = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

max_a = a[0][0]
max_i = max_j = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] > max_a:
            max_a = a[i][j]
            max_i = i
            max_j = j

print(max_i, max_j)
