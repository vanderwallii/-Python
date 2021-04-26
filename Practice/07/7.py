import math

def input_vertices(message):
    val = list(map(float, (input(message).split())))

    if len(val) == 2:
        return val
    raise ValueError
    
def vertices_calculate(a, b, c):
    x1 = a[0] - c[0]
    x2 = b[0] - c[0]
    y1 = a[1] - c[1]
    y2 = b[1] - c[1]
    return math.fabs(x1*y2-x2*y1)/2   
    
print("1-длины сторон, 2-координаты вершин")
figure = input("Выберите тип ввода: ")
 
if figure == '1':
    
    print("Длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    p = (a + b + c) / 2
    from math import sqrt
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь: %.2f" % s)
       
elif figure == '2':
    
    print("Координаты вершин треугольника:")
    a = input_vertices('Введите координаты вершины A: ')
    b = input_vertices('Введите координаты вершины B: ')
    c = input_vertices('Введите координаты вершины C: ')
    print('Площадь =', vertices_calculate(a, b, c))
    
else:
    print("Ошибка ввода")
    

