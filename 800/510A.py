inp = list(map(int, input().split()))

height = 0
snake = ''
right = True

while height != inp[0]:
  if height == 0 or height % 2 == 0: snake += '#' * inp[1] + '\n'
  else:
    if right: 
      snake += (inp[1] - 1) * '.' + '#' + '\n'
      right = False
    else: 
      snake += '#' + (inp[1] - 1) * '.' + '\n'
      right = True
  height += 1

print(snake)