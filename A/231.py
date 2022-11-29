n = int(input())
p = 0
for i in range(n):
  inp = list(map(int, input().split()))
  if inp.count(1) > 1: p += 1
print(p)