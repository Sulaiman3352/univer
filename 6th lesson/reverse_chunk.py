char_to_find = 'f'
s = input("input string with symble" + char_to_find + ":/n")
pos1 = s.find(char_to_find)
pos2 = s.rfind(char_to_find )

print(s[:pos1 + 1] + s[pos2:pos2 + 1 :-1] + s[pos2:])