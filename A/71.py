# Way Too Long Words
test_cases = int(input())
for i in range(test_cases):
  inp = str(input())

  if len(inp) > 10: print(f'{inp[0]}{str(len(inp)-2)}{inp[-1]}')
  else: print(inp)
