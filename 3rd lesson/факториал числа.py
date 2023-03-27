n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

for j in range(n1, n2+1):
    ans = 1
    for i in range(2, j +1 ):
        ans = ans *i
    print("factorial of", j, "is", ans)