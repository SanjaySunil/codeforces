string = input()
upper = 0
for i in string:
  if i.isupper(): upper += 1
print(string.lower()) if upper <= len(string) - upper else print(string.upper())
