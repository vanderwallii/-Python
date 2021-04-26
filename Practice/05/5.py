# ускорение свободного падения
g = 9.8

# функция для ввода значений
def input_value():
   
        x0, v0, t = map(float, input("Введите x0,v0,t: ").split())
        print(distance_calculation(x0, v0, t))
    
        input_value()
# функция для расчета расстояния 
def distance_calculation(x0, v0, t):
    return x0 * v0 * t - g * t ** 2
input_value()