x = int(input())
passengers = 0
max_passengers = 0
for _ in range(x):
  arr = list(map(int, input().split()))
  passengers -= arr[0]
  passengers += arr[1]
  if passengers > max_passengers: max_passengers = passengers

print(max_passengers)