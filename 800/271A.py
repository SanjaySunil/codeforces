year = int(input())
new = year + 1

while list(sorted(str(new))) != list(sorted(set(str(new)))): new += 1

print(new)