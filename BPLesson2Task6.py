goods = []
number = 1
while True:
    print ("Ввод данных для товара ", number)
    name = input("Введите название товара ")
    price = int(input("Введите цену товара "))
    quantity = int(input("Введите количество товара "))
    measure = input("Введите единицу измерения товара ")
    goods.append((number, {"Название":name, "Цена":price, "Количество":quantity, "Единица":measure}))
    number += 1
    stop = input("Чтобы закончить ввод данных о товарах, введите exit, а чтобы продолжить, нажмите на любую клавишу: ")
    if stop == "exit":
        break
print("\n", "Получилась следуюущая структура данных о товарах: ", "\n", goods)
goods2 = []
for item in goods:
    goods2.append(item[1])
name = []
price = []
quantity = []
measure = []
for dicts in goods2:
    if dicts.get("Название") not in name:
        name.append(dicts.get("Название"))
    if dicts.get("Цена") not in price:
        price.append(dicts.get("Цена"))
    if dicts.get("Количество") not in quantity:
        quantity.append(dicts.get("Количество"))
    if dicts.get("Единица") not in measure:
        measure.append(dicts.get('Единица'))
finaldict = {"Название":name, "Цена":price, "Количество":quantity, "Единица":measure}
print("\n", "Получился следующий итоговый словарь: ", "\n", finaldict)
input()