# Petya and Strings
one = list(input().lower())
two = list(input().lower())

for i in range(len(one)):
  if ord(one[i]) > ord(two[i]): 
    print(1)
    exit()
  elif ord(one[i]) < ord(two[i]): 
    print(-1)
    exit()

print(0)