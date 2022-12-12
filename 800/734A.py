x = int(input())
string = str(input())

if string.count('A') > string.count('D'): print('Anton')
elif string.count('A') < string.count('D'): print('Danik')
else: print('Friendship')