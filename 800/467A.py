rooms = int(input())
available = 0
for i in range(rooms):
  inp = list(map(int, input().split()))
  if inp[-1] - inp[0] >= 2: available += 1
print(available)