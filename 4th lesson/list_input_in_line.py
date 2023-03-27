lst = []
n = int(input("How may numbers in list? "))
print("input", n, "numbers in single line with spaces")
#lst = [int(s) for s in input().split()]
lst = list(map(int, input().split()))
print(lst)