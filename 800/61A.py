one = list(map(int, input()))
two = list(map(int, input()))
ans = ''
for i in range(len(one)):
  if one[i] == 0 and two[i] == 0 or one[i] == 1 and two[i] == 1: ans += '0'
  else: ans += '1'
print(ans)