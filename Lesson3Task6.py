def int_func(text):
    while True:
        text = input('Введите слово или строку из слов, написанных латинскими буквами в нижнем регистре, разделенных пробелами: ')
        ord_list = []
        for letter in text:
            ord_list.append(ord(letter))
        for element in ord_list:
            if element in range(97, 123) or element == 32:
                continue
            else:
                print('You shall not pass! Нужны слова, написанные именно маленькими латинскими буквами!')
                break
        else:
            break
    return text.title()

text = "text"
print(f"Хотели большие первые буквы? Получите и распишитесь: { int_func(text)}")
input()