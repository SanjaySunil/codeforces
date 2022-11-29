# Domino piling
inp = list(map(int, input().split()))
spaces = inp[0] * inp[1]
pieces = 0
while spaces > 1:
  spaces -= 2
  pieces += 1
print(pieces)