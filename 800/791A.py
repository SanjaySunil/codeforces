arr = list(map(int, input().split()))
yrs = 0
while arr[0] <= arr[1]:
  arr[0] *= 3
  arr[1] *= 2
  yrs+=1
print(yrs)