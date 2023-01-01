inp = [input() for i in range(3)]

print('YES') if sorted(inp[0] + inp[1]) == sorted(inp[2]) else print('NO')