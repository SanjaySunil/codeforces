n = int(input())
stones = list(input())

flag = False

while flag == False:
  flag = True
  curr = 0
  while curr != len(stones) - 1:
    if curr + 1 == len(stones): break
    if stones[curr] == stones[curr+1]:
      stones.pop(curr)
      curr -= 1
      flag = False
    curr += 1

print(n - len(stones))
