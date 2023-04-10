# Условие
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.


char_to_find = 'f'
s = input("input string with symble" + char_to_find + ":/n")
pos1 = s.find(char_to_find)
pos2 = s.rfind(char_to_find )

print(s[:pos1] + s[pos2 + 1:])