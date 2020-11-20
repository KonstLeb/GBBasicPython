from random import randint
initial_list = []

while True:
    try:
        number_of_elements = int(input("Список из скольких случайных чисел Вы хотите сформировать? Введите значение от 2 до 1000: "))
        if number_of_elements not in range(2, 1001):
            print("Неужели трудно ввести число в указанном диапазоне?")
            continue
    except ValueError:
        print("Если Вы снова введете не число, я сделаю что-нибудь страшное! Например, зарыдаю!")
    else:
        break
    
initial_list = [randint(0,1000) for element in range(0, number_of_elements)]
final_list = [el for el in initial_list if el > initial_list[initial_list.index(el) - 1] and initial_list.index(el) != 0]
print (f"Был сгенерирован такой начальный список чисел: \n{initial_list}\n")
print(f"А это список чисел из начального списка, значения которых больше предыдущего элемента: \n{final_list}")
input()
