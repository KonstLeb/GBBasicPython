revenue = int(input("Введите величину выручки фирмы в рублях:"))
cost = int(input("Введите величину издержек фирмы в рублях:"))
if revenue < cost:
    print (f"Фирма отработала с убытком в размере {cost - revenue} рублей")
elif revenue == cost:
    print ("Фирма отработала с нулевым результатом")
else:
    print (f"Фирма отработала с прибылью в размере {revenue - cost} рублей")
    print (f"Рентабельность выручки составляет {((revenue - cost) / revenue):.03f}")
    stuff = int(input("Укажите численность сотрудников фирмы: "))
    print (f"Прибыль фирмы в расчете на одного сотрудника составляет {((revenue - cost) / stuff):.02f} рублей")
input()
