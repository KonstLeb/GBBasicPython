my_list = [4,5,6,8,3,4,5,5,6,25,23,6,5,4]
my_list.sort(reverse = True)
print('Исходный рейтинг выглядит так: ', my_list)
try:
    n = int(input("Введите новый элемент рейтинга (натуральное число): "))
except ValueError:
    n = int(input("Пожалуйста, таки сосредоточьтесь и введите новый элемент рейтинга (натуральное число): "))
my_list.append(n)
my_list.sort(reverse = True)
print('Отсортированный список с учетом введенного значения выглядит так: ', my_list)
input()