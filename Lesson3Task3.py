def my_func(a, b, c):
    sum = (a + b + c) - min(a, b, c)
    return (f"Сумма двух наибольших чисел составляет {sum}")

while True:
    try:
        a = float(input("Введите первое число: "))
    except ValueError:
        print("С этим так называемым числом мы далеко не уедем, исправьтесь!")  
    else:
        break
while True:
    try:
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Покайтесь и введите ЧИСЛО!!")  
    else:
        break
while True:
    try:
        c = float(input("Введите третье число: "))
    except ValueError:
        print("Числа так не выглядят, сосредоточьтесь!!!") 
    else:
        break
        
print(my_func(a, b, c))
input()