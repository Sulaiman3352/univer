s = input().split()
a = [int(x) for x in s]
a_max = max(a)
i_max = 0

for i in range(0, len(a)):
    if a[i] > a_max:
        a_max = a[i]
        i_max = i
print(a_max, i_max) 