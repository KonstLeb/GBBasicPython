def division (a, b):
    
    while True:
        try:
            a = float(input("Введите делимое: "))
        except ValueError:
           print("Делить можно только числа, а всякие другие знаки не поделишь! Исправьтесь!")
        else:
            break
    while True:
        try:
            b = float(input("Введите делитель: "))
        except ValueError:
           print("За неправильный делитель попадают в вытрезвитель! Давайте же число!")
        else:
            break     
    try:
        c = float(round((a / b), 2))
        return (f"Частное: {c}")
    except ZeroDivisionError:
        return

a = 0
b = 0
print(division (a, b))
input()