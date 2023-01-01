n = int(input())
events = list(map(int, input().split()))
officers = 0
crimes = 0
for i in range(len(events)):
  if events[i] > 0: officers += events[i]
  else:
    if events[i] == -1 and officers == 0: crimes += 1
    else: officers -= 1
print(crimes)