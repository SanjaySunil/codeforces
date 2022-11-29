# Helpful Maths
inp = list(input())
while '+' in inp: inp.remove('+')
inp = list(sorted(inp))
string = inp[0]
for i in range(1, len(inp)): string += '+' + inp[i]
print(string)