n = int(input("How may numbers in list? "))
print("input", n, "numbers in single line with spaces")
a = [int(s) for s in input().split()]

min_a = a[0]
max_a = a[0]

max_a = max(a)
min_a = min(a)

print("max_a =", max_a)
print("min_a =", min_a)