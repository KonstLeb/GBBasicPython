from random import randint
initial_list = []
while True:
    try:
        number_of_elements = int(input("Список из скольких случайных чисел Вы хотите сформировать? Введите значение от 20 до 100: "))
        if number_of_elements not in range(20, 101):
            print("Неужели трудно ввести число в указанном диапазоне?")
            continue
    except ValueError:
        print("Если Вы снова введете не число, я сделаю что-нибудь страшное! Например, зарыдаю!")
    else:
        break
initial_list = [randint(1,51) for element in range(0, number_of_elements)]
final_list = [el for el in initial_list if initial_list.count(el) == 1]
print (f"Был сгенерирован такой начальный список чисел: \n{initial_list}\n")
print(f"А это список чисел из начального списка, которые встречаются только один раз: \n{final_list}")
input()
