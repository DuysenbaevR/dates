# Выведите на экран текущий день.
# Выведите на экран текущий месяц.
# Выведите на экран текущий год
# Выведите на экран номер текущего дня недели
import datetime
import locale
locale.setlocale(locale.LC_ALL, "UZ")

data = datetime.datetime.now()
print(data.strftime("%d"))
print(data.strftime("%B"))
print(data.strftime("%Y"))
print(data.strftime("%A"))