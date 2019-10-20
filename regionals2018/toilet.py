s = input()
print(s[1:].count('D')*2 if s[0] == 'U' else s[1:].count('D')*2-1)
print(s[1:].count('U')*2 if s[0] == 'D' else s[1:].count('U')*2-1)
print(s[1:].count('UD') + s[1:].count('DU'))