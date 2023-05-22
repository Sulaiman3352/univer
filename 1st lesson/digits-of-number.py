a = int(input("input three digits for a :"))

if a < 100:
    print("a is too small")
elif a > 999:
    print(" a is too big")
else:
    print(" 1st digit =", a //100)
    print(" 2st digit =", a // 10%10)
    print(" 3st digit =", a %10)