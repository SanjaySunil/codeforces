n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print('I become the guy.') if len(set(x[1:] + y[1:])) == n else print('Oh, my keyboard!')