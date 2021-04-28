import re

quantity = int(input("Введите количество билетов Сигизмунда в промежутке 1 <= x <= 10^9: "))
if 1 <= quantity <= 10 ** 9:
    tickets = input("Введите билеты через пробел: ").split(' ')
    
    regex = r"(^a[a-z0-9]{3}55661)"
    a = re.compile(regex) 
    
    result = list(filter(a.match, tickets))
    
    if len(result) == 0:
     print(-1)
    else:
     print(*result, sep=' ')