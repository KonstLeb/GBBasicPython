number = input("Введите целое положительное число: ")
maximum = number[0]
k = 1
while k < len(number):
    if number[k] > maximum:
        maximum = number[k]
    k += 1
print (f"Самая большая цифра в числе {number} - это {maximum}")
input()
