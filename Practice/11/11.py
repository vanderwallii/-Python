def raise_power(n, power):
    a = n
    while power > 1:
        n *= a
        power -= 1
    return n

number = float(input("Введите число: "))    
power = int(input("Введите степень: "))
print(raise_power(number, power))