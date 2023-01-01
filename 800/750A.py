inp = list(map(int, input().split()))

remaining = 240 - inp[-1]
problems = 0

for i in range(1, inp[0]+1):
  if remaining - (5 * i) < 0: break
  else: 
    problems += 1
    remaining = remaining - (5 * i)

print(problems)