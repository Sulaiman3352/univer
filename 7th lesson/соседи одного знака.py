s = input().split()
a = [int(x) for x in s]
for i in range(1, len(a)-1):
    if a[i + 1] > 0 and a[i - 1] > 0:
        print(a[i], end=" ")

    if a[i + 1] < 0 and a[i - 1] < 0:
        print(a[i], end=" ")