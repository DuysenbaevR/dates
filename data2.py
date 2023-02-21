#2) Выведите на экран текущий месяц словом, по-русски.
import datetime
import locale
locale.setlocale(locale.LC_ALL, "ru")

data = datetime.datetime.now()
print(data.strftime("%B"))