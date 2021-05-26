W,H = map(float,input().split())

def BMI(W: float, H: float) -> float:

    return W/(H/100)**2

def print_BMI(BMI: float):

    if(BMI < 18.5):
        print("Underweight")
    elif(BMI >= 18.5 and BMI < 25.0):
        print("Normal")
    elif(BMI >= 25.0 and BMI < 30.0):
        print("Overweight")
    elif(BMI >= 30.0):
        print("Obesity")
    else:
        print("Повторите ввод!")
        
print_BMI(BMI(W,H))