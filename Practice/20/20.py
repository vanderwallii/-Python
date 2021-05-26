Cash, a = int(input()), int(input())
Result = [0] * a
liters = [0] * a
Alco = [0] * a
Price = [0] * a
f = [0] * a
c = 0

for i in range (a) :
    Alco[i], Price[i], f[i] = map(str, input().split(' '))
    Price[i] = int(Price[i])
    f[i] = int(f[i])
    Result[i] = int(Cash / Price[i])
    liters[i] = Result[i] * f[i]
    if liters[i] == 0 : c = c + 1

if c == a :
    print(-1)
    exit(0)

for i in range (a) :
    for j in range (a) :
        if liters[i] > liters[j] : k = i

print(Alco[k], Result[k])
print(liters[k])
print(Cash - (Price[k] * Result[k]))