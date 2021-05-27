def inp_num():

    global main_num

    try:
        num = int(input("Введите число - "))
        
        if not 1 <= num <= 10 ** 9:
            raise ValueError
        for i in range(2, num):
            t = check_main(i)
            
            if t != 0:
                main_num.append(t)
        print_factorization(num)

    except ValueError:
        print("Введите другое число!")
        

def check_main(m):

    t = 2

    while m % t != 0:
        t += 1

    if t == m:
        return m

    else:
        return 0


def dec_num(num, res):

    for main in main_num:

        if num % main == 0:
            num = num / main

            if main in res:
                res[main] += 1

            else:
                res[main] = 1
            return dec_num(num, res)

    if num > 1:
        res[num] = 1


def print_factorization(m: int):
    
    res = {}
    r = ""
    dec_num(m, res)
        
    for i in res:

        if res[i] > 1:
            r += '*' + str(i) + '^' + str(res[i])
        else:
            r += '*' + str(i)
    r = r[1:len(r)]

    print(r)
main_num = []
inp_num()


