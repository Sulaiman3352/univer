s = input().split()
a = [int(x) for x in s ]

for i in range(0, len(a)):
    if a[i] % 2 == 0:
        print(a[i], end=" ")