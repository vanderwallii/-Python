def find_quantity(n):
    temp = 0
    while 2**temp <= n:
        temp += 1
    return temp

num = int(input("Введите целое число: "))
print(find_quantity(num))