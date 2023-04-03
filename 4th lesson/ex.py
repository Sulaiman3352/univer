n = int(input("How may numbers in list? "))
print("input", n, "numbers in single line with spaces")
a = [int(s) for s in input().split()]

max_a = max(a)
max_2 = 0

for i in range(0, n):
    if a[i] > max_2:
        if a[i] < max_a:
            max_2=a[i]

print(max_a, max_2)

