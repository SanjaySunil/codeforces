inp = [int(input()) for i in range(5)]
count = 0   
for i in range(inp[-1]+1):
  if i % inp[0] == 0 and i >= inp[0] or i % inp[1] == 0 and i >= inp[1] or i % inp[2] == 0 and i >= inp[2] or i % inp[3] == 0 and i >= inp[3]:
    count += 1

print(count)