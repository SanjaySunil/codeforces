inp = list(map(int, input().split()))
hipster = 0
match = 0
while inp[0] > 0 or inp[1] > 0:
  if inp[0] > 0 and inp[1] > 0:
    inp[0] -= 1
    inp[1] -= 1
    hipster += 1
  elif inp[0] > 1:
    inp[0] -= 2
    match += 1
  elif inp[1] > 1:
    inp[1] -= 2
    match += 1
  else: break
print(hipster, match)
