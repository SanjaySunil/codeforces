tc = int(input())
answers = []
for _ in range(tc):
  inp = input()
  answers.append(int(inp[0]) + int(inp[2]))
[print(i) for i in answers]