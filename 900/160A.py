n = int(input())
coins = sorted(list(map(int, input().split())))
cost = 0
coin = -1
while cost <= sum(coins):
  cost += coins[-1]
  coins.pop()
print(n - len(coins))