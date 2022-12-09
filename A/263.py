arr = []
for _ in range(5): arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            2, 2
            1, 4
            print(abs(2-i) + abs(2 - j))
