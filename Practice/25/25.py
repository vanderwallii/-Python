import random
from math import sqrt

def input_num():
 
        n = int(input("Введите количество чисел n (4<=n<=100): "))

        if 4 <= n <= 100:
            num = list(map(int, input(f"Введите несколько {n} чисел: ").split(' ')))
            if len(num) != n:
                print("Не подходящее количество чисел!")
                raise ValueError

            print(*BozoSort(num), s=' ')

            print(*BozoSort(num, False), s=' ')

            size = int(sqrt(n))
            array = []
            for i in range(0, size):
                array.append(num[i*size:(i*size)+size])

            print(*BozoSort(array), s=' ')

            print(*BozoSort(array, False), s=' ')

            print(*BozoSort(num[0:3]), s=' ')

            print(*BozoSort(num[0:3], False), s=' ')

        else:
            print('Неверное количество чисел')
            raise ValueError

def BozoSort(val, asc=True):
    
    if isinstance(val[0], list):
        t = []
        for i in val:
            for j in i:
                t.append(j)
        val = t
  
    i1 = random.randint(0, len(val)-1)

    i2 = random.randint(0, len(val)-1)
    
    while i1 == i2:
        i2 = random.randint(0, len(val)-1)

    val[i1], val[i2] = val[i2], val[i1]

    for i in range(0, len(val)):
        if i >= len(val) - 1:
            return val
        elif asc:
            if val[i] > val[i+1]:
                return BozoSort(val, asc)
        else:
            if val[i] < val[i+1]:
                return BozoSort(val, asc)


