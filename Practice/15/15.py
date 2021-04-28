import random
try_user = 0


number = random.randint(1, 100)
print ("Угадайте число между 1 и 100. У вас есть 5 попыток")

while try_user < 5:

    guess = int(input("Введите число: "))
    try_user += 1

    if guess < number:
        print ("Загаданное число больше")

    if guess > number:
        print ("Загаданное число меньше")

    if guess == number:
        break

if guess == number:
    print ('Поздравляю! Вы угадали, использовав {0} попыток!'.format(guesses_made))
           
else:
    print ('Вы проиграли. Было загадано: {0}'.format(number))