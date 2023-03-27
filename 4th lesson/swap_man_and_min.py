n = int(input("How may numbers in list? "))
print("input", n, "numbers in single line with spaces")
a = [int(s) for s in input().split()]
min_a = max_a = a[0]
ind_min = ind_max = 0
for i in range(1, n):
    if a[i] > max_a:
        max_a = max[a]; ind_max = i
    if a[i] < min_a:
        min_a = a[i]; ind_min = i
a[ind_max] = min_a
a[ind_min] = max_a
print(a)