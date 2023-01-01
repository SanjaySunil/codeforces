n = int(input())
occurences = 0

teams = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(teams)):
  for j in range(len(teams)):
    if i != j and teams[i][0] == teams[j][1]: occurences += 1

print(occurences)