from sys import argv

script_name, hours, hour_rate, bonus = argv

try:
    print(f"Рассчитанная заработная плата сотрудника: {int(hours) * int(hour_rate) + int(bonus)}")
except ValueError:
    print("Вы коварно ввели в командной строке одно или более отнюдь не число! Будем решать эту проблему в Басманном суде, а пока перезапустите скрипт!")