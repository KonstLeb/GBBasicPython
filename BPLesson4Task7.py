def fact(n):
    import math
    while True:
        try:
            n = int(input("Введите целое положительное число: "))
            if n <= 0:
                print("Положительные люди вводят ПОЛОЖИТЕЛЬНЫЕ числа! Попробуйте снова!")
            else:
                break
        except ValueError:
            print("Конечно, отличать другие знаки от чисел - большое искусство, но постарайтесь сосредоточиться!")
    for element in range(1, n+1):
        yield f'Факториал числа {element} равен {math.factorial(element)}'

n = None            
for el in fact(n):
    print(el)
input()