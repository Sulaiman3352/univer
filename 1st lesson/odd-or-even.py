a = int(input(" A = "))
b = int(input(" B = "))
if a % 2 == 0 and b % 2 != 0:
    print("No")
elif a % 2 != 0 and b % 2 == 0:
    print("No")
elif a % 2 != 0 and b % 2 != 0:
    print("yes")
elif a % 2 == 0 and b % 2 == 0:
    print("yes")