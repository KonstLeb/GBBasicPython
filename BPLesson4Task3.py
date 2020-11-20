print(f'В пределах от 20 до 240 на 20 или 21 без остатка делятся следующие числа: \n{[element for element in range(20, 241) if element%20 == 0 or element%21 ==0]}')
input()