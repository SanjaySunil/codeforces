params = list(map(int, input().split()))

for i in range(params[-1]): 
  if str(params[0])[-1] != '0': params[0] -= 1
  else: params[0] //= 10

print(params[0])