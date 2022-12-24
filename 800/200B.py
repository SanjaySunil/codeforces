n = int(input())
drinks = list(map(int, input().split()))
sum = 0
for i in range(n):
  if drinks[i] != 0: sum += 1 / (100 / drinks[i])
print((sum/n) * 100)