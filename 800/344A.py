magnets = int(input())
groups = 1
previous = ''
for i in range(magnets):
  if i == 0: previous = input()
  else:
    magnet = input()
    if magnet != previous: 
      groups += 1
      previous = magnet

print(groups)