def conv(value, m, f) -> str:
    pin = ''
    while value > 0:
        pin += str(value % f)
        value //= f

    return pin[::-1].zfill(m)

while True:
    try:
        m = int(input())
        f = tuple(input())

        if m < 1 or m > 8:
            print("Число n не соответствует параметрам m < 1, m > 8")
            continue

        if len(f) < 1 or len(f) > m: 
            print("Длина строки < 1 или > n")
            continue

        pin = [conv(x, m, len(f)) for x in range(len(f) ** m)] 

        symbols = set([str(x) for x in range(len(f))])
        pin = [x for x in pin if set(x) == symbols] 
        pin = ' '.join([''.join(f[int(j)] for j in r) for r in pin])  

        print(pin)

        break

    except KeyboardInterrupt:
        break
    except ValueError:
        print("Повторите ввод!")