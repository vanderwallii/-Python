example = input("Введите выражение:") #5 + 6
number_1, operation, number_2 = example.split() #split разбивает строку на три состовляющих
number_1 = float(number_1)
number_2 = float(number_2)

if operation == '+':
 print('{} + {} = '.format(number_1, number_2))
 print(number_1 + number_2)
      
elif operation == '-': 
 print('{} - {} = '.format(number_1, number_2))
 print(number_1 - number_2)
 
elif operation == '*':
 print('{} * {} = '.format(number_1, number_2))
 print(number_1 * number_2)
 
elif operation == '/':
 print('{} / {} = '.format(number_1, number_2))
 print(number_1 / number_2)

else:
 print ("Не верно введено выражение")