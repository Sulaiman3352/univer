s = input('input text: ')
n = len(s)//2
if len(s)%2 == 0:
    print(s[-n:],s[:n], sep="")
else:
    print(s[-n:],s[:n+1], sep="")
