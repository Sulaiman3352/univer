s = input().split()
a = [int(x) for x in s]
k = 1

for i in range(0, len(a)-1):
    if a[i] < a[i+1]:
        k += 1
print(k)