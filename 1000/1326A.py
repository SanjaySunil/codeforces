test = int(input())
 
for _ in range(test):
  num = int(input())
  
  if num == 1: print(-1)
  else:
    print(str(2) + str((num - 1) * '3'))