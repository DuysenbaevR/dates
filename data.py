#1)Выведите на экран текущие день, месяц и год в формате 'год-месяц-день'.

import datetime
import locale
locale.setlocale(locale.LC_ALL, "ru")

data = datetime.datetime.now()
print(data.strftime("%Y-%m-%d"))