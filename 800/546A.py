params = list(map(int, input().split()))
k = params[0]
n = params[1]
w = params[2]

got = 0
cost = 0

while got != w:
  cost += (got + 1) * params[0]
  got += 1

if cost - n < 0: print(0)
else: print(cost - n)