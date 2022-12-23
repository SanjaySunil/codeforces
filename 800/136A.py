friends = int(input())
gifts = list(map(int, input().split()))

print(" ".join(map(str, [gifts.index(i)+1 for i in range(1, len(gifts)+1)])))