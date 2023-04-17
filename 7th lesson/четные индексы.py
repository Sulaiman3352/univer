s = input().split()
a = [int(x) for x in s ]

for i in range(0, len(a), 2):
    print(a[i], end="")