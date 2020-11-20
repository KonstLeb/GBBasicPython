from sys import argv
script_name, first, second = argv
def numbers(first, second):
    try:
        int(first)
        int(second)
    except ValueError:
        print("Вы коварно ввели в командной строке одно или более отнюдь не число! Будем решать эту проблему в Басманном суде, а пока перезапустите скрипт!")
        exit()
    print("Генератор нагенерировал вот что: ")
    from itertools import count
    for i in count(int(first)):
        if i > int(second):
            break
        else:
            print (i)
numbers (first, second)