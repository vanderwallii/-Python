words = ("hallo", "klempner", "das", "ist", "fantastisch", "fluggegecheimen")

hidden = str(input())

symbol = [0] * 26

a = ord('a')

for word in words:
    for c in word:
        symbol[ord(c) - a] += 1

case = 1
full = sum(symbol)

for c in hidden:
    case *= symbol[ord(c) - a] / full
    if (case == 0): break

print(case)