params = list(map(int, input().split()))
queue = list(input())

for i in range(params[-1]):
  curr = 0
  while curr < len(queue) - 1:
    if queue[curr + 1] == 'G' and queue[curr] == 'B':
      queue[curr] = 'G'
      queue[curr+1] = 'B'
      curr += 2
    else: curr += 1

print("".join(queue))