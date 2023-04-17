s = input().split()
a = [int(x) for x in s]

a_max = a_min = a[0]
i_max = i_min = 0

for i in range(0, len(a)):
    if a[i] > a_max :
        a_max = a[i]
        i_min = i
    if a[i] < a_min:
        a_min = a[i]
        i_min = i
a[i_max], a[i_min] = a[i_min], a[i_max]

print(a)