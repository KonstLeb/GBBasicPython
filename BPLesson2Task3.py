# c помощью списков
print ("Сейчас мы займемся определением сезона с помощью списка (list)!")
seasons = [["ЗИМА", "1", "2", "12"], ["ВЕСНА", "3", "4", "5"], ["ЛЕТО", "6", "7", "8"], ["ОСЕНЬ", "9", "10", "11"]]
month = "0"
while month.isdigit() == False or int(month) not in range (1, 13):
    month = input ("Введите номер месяца (от 1 до 12): ")
for season in seasons:
    if month in season:
        print (f'Капитан Очевидность сообщает, что месяц {month} относится к сезону {season[0]}! Будьте здоровы!')
# c помощью словарей
print ("А сейчас мы займемся определением сезона с помощью словаря (dict)!")
seasons = {"1":"ЗИМА", "2":"ЗИМА", "12":"ЗИМА", "3":"ВЕСНА", "4":"ВЕСНА", "5":"ВЕСНА", "6":"ЛЕТО", "7":"ЛЕТО", "8":"ЛЕТО", "9":"ОСЕНЬ", "10":"ОСЕНЬ", "11":"ОСЕНЬ"} 
month = 0
while month not in (seasons.keys()):
    month = input ("Введите номер месяца (от 1 до 12): ")
print (f'Капитан Очевидность сообщает, что месяц {month} относится к сезону {seasons.get(month)}! Будьте здоровы!')
input()