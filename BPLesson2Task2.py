mylist = []
while True:
    element = input("Введите элемент списка. Если хотите прекратить ввод элементов, введите exit: ")
    if element == "exit":
        break
    else: 
        mylist.append(element)
print (f"Сформирован исходный список: {mylist}")

for index in range (0, len(mylist) - 1, 2):
        mylist[index], mylist[index + 1] = mylist[index + 1], mylist[index]
print (f"А вот список с перестановкой элементов: {mylist}")
input()