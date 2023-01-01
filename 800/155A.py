n = int(input())
points = list(map(int, input().split()))
best = points[0]
worst = points[0]
amazing = 0
for i in range(1, len(points)):
  if points[i] > best: 
    amazing += 1
    best = points[i]
  if points[i] < worst: 
    amazing += 1
    worst = points[i]
print(amazing)