n = int(input())
soldiers = list(map(int, input().split()))
moves = 0
max_height = -1
min_height = -1
  
max_height = [i for i in range(0, len(soldiers)) if soldiers[i] == max(soldiers) and max_height == -1]

while max_height[0] != 0:
  temp = soldiers[max_height[0]]
  soldiers[max_height[0]] = soldiers[max_height[0] - 1]
  soldiers[max_height[0] - 1] = temp
  max_height[0] -= 1
  moves += 1

for i in range(len(soldiers)):
  if soldiers[i] == min(soldiers): min_height = i

while min_height != len(soldiers) - 1:
  temp = soldiers[min_height]
  soldiers[min_height] = soldiers[min_height + 1]
  soldiers[min_height + 1] = temp
  min_height += 1
  moves += 1

print(moves)