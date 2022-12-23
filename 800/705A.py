n = int(input())

res = ''

if n == 1:
    print('I hate it')
    exit()

for i in range(1, n):
    if i % 2 == 0:
        res += 'I love that '
    else:
        res += "I hate that "

if n % 2 == 0:
    print(res + 'I love it')
else:
    print(res + 'I hate it')
