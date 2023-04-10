s = input("input: ")
Symbol_to_find = "h"
Symbol_to_replace = "H"

pos1 = s.find(Symbol_to_find)
pos2 = s.rfind(Symbol_to_find)

s1 = s[:pos1 + 1 ] + s[pos1 +1 : pos2].replace(Symbol_to_find, Symbol_to_replace) + s[pos2:]

print(s1)