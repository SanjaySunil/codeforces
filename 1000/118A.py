string = list(input().lower())
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

curr = 0

while curr != len(string):
  if string[curr].lower() in vowels:
    string.pop(curr)
    curr -= 1
  elif string[curr] not in vowels and string[curr-1] != '.': string.insert(curr, '.')
  curr += 1

print("".join(string))