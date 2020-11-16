def my_func(x,y):
    z = x
    for i in range(1, (abs(y))):
        x = x * z
    final_number = round(1 / x, 10)
    return (f"Число {z} в степени {y} равно {final_number}")

while True:
    try:
        x = float(input("Введите положительное число, которое собираетесь возвести в степень: "))
        while True:
            if x <= 0:
                x = float(input("Введите положительное число, которое собираетесь возвести в степень: "))
            else:
                break
    except ValueError:
        print("Прекратите хулиганить! Вместо абракадабры введите число!")
    else:
        break
        
while True:
    try:
        y = int(input("Введите целое отрицательное число (степень, в которую нужно возвести число): "))
        while True:
            if y >= 0:
                y = int(input("Введите целое отрицательное число (степень, в которую нужно возвести число): "))
            else:
                break
    except ValueError:
        print("Прекратите хулиганить, вместо абракадабры введите число!")
    else:
        break
        
print(my_func(x,y))
input()