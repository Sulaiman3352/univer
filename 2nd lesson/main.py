n = int(input())
ans = ""
s1 = input()

while n > 1:
    s = input()
    if len(s) > len(s1):
        ans = ans + s + "\n"

    n = n - 1

print("ALL LINES lonfger than first line: \n", ans)