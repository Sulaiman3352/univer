n1 = int(input("N1 = "))
n2 = int(input("N2 = "))

if n2 < n1 :
    n2, n1 = n1, n2

for i in range (n1, n2+1):
    #print(i, end=" ")
    #prime = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
     #       print(" - not prime")
            #prime = False
            break
    else:
        print(i, "- prime")