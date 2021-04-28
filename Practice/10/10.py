def search_pare(r1, r2, l1, l2, a):
    if r1[l1] + r2[l2] == a:
        return [r1[l1], r2[l2]]
    else:
        l2 += 1
        if l2 < len(r2):
            return search_pare(r1, r2, l1, l2, a)
        else:
            l1 += 1
            l2 = 0
            if l1 < len(r1):
                return search_pare(r1, r2, l1, l2, a)
            else:
                return -1

num = list(map(int, input('Введите числа: ').split()))
r1 = num[1:3]
r2 = num[3:5]

if r1[0] + r2[0] <= num[0] <= r1[1] + r2[1]:
    print(*search_pare(r1, r2, 0, 0, num[0]))
else:
    print(-1)