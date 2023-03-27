n = int(input("How may numbers in list? "))
print("input", n, "numbers in single line with spaces")
a = [int(s) for s in input().split()]
min_a = max_a = a[0]
ind_min = ind_max = 0

ind_max = a.index(max(a))
ind_min = a.index(min(a))

a[ind_max], a[ind_min] = min_a, max_a

print(a)