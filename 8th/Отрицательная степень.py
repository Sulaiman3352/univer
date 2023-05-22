def power(a, n) :
    if n ==0:
        return 1
    p = 1
    if n > 0:
        for i in range(n):
            p = p * a
    else: # n <0
        for i in range(abs(n)):
            p = p / a
    return p


a, n = float(input()), int(input())
print(power(a, n))
# print("ok" if power(a, n) == 32768 else "bad")