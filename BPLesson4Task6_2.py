from sys import argv

script_name, number_of_iterations = argv

def povtor(number_of_iterations):

    try:
        int(number_of_iterations)
    except ValueError: 
        print("Вы злодейски ввели в командной строке отнюдь не целое положительное число! Это было обидно! Перезапустите скрипт!")
        exit()
        
    list = [3, 2, 2, "да", 2, 2, 3, "домомучительница", "карлсон"]
    print(f"Элементы заранее определенного списка в количестве {number_of_iterations} штук: ")
    import itertools
    count = 0
    for item in itertools.cycle(list):
        if count > int(number_of_iterations):
            break
        print (item)
        count += 1
         
povtor (number_of_iterations)