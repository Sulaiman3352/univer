s = input().split()
a = [int(x) for x in s]

for i in range(0, len(a)-1,2):
    a[i], a[i+1] = a[i+1], a[i]

print(a)