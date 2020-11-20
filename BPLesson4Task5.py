initial_list = [el for el in range(100, 1001) if el%2 == 0]
print (f"Получился такой исходный список: \n{initial_list}\n")
from functools import reduce
total =  reduce(
        lambda itogo, number: itogo * number, initial_list
)
print("Получилось такое произведение всех элементов списка: ")
print(total)
input()