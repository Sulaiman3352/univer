s = input().split()
a = [int(x) for x in s]
for i in range(1, len(a)):
    if a[i] > a [i - 1]:
        print(a[i], end=" ")

