timesec = int (input ("Введите время в секундах: "))
hours = timesec // 3600
minutes = (timesec - hours*3600) // 60
seconds = (timesec - hours*3600) % 60
print (f"{hours:02d}:{minutes:02d}:{seconds:02d}")
input()