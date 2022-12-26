n = int(input())
string = input().lower()

print('YES') if sorted(set(string)) == [chr(i) for i in range(97, 123)] else print('NO')