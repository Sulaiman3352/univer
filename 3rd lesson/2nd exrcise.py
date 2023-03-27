n1 = int(input("N1 = "))
n2 = int(input("N2 = "))

s1 = 0
s2 = 0
for i in range(n1, n2+1):
    s1 = s1 + i
for i in range(n1, n2+1):
    s2 = s2 + i

if n1 % 2 != 0:
    s1, s2 = s2, s1

print("S1 = ", s1, ", S2 =", s2)