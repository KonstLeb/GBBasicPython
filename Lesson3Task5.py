def string_count(string_of_numbers):
    global summa
    break_on = 0
    while True:
        if break_on == 1:
            break
        else:
            string_of_numbers = input("Введите строку ЧИСЕЛ, разделенных ПРОБЕЛАМИ!"+"\n"+"После завершения нажмите Enter."+"\n"+"После каждого нажатия Enter будет подсчитана промежуточная сумма"+"\n"+"Затем Вы можете продолжить ввод чисел."+"\n"+"Если хотите подсчитать итоговую сумму, введите @ через пробел после последнего числа."+"\n")
            list_of_numbers = string_of_numbers.split()
            for number in list_of_numbers:
                if number == "@":
                    break_on = 1
                    print ("Программа завершена, подсчитана итоговая сумма чисел!")
                    break
                else:
                    try:
                        summa = summa + float (number)
                    except ValueError:
                        continue
            print (f"Сумма чисел составляет: {summa}")

summa = 0
string_of_numbers = ''
string_count(string_of_numbers)
input()