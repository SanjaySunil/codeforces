# Bit++
operations = int(input())
res = 0
for i in range(0, operations):
  inp = input()
  if inp.lower() == '++x' or inp.lower() == 'x++': res+=1
  elif inp.lower() == '--x' or inp.lower() == 'x--': res-=1
print(res)