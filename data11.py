#11)  Напишите функцию formatDate(date),
# которая выводит дату date в формате дд.мм.гг
import datetime
import locale
locale.setlocale(locale.LC_ALL)

date = datetime.datetime.now()
print(date.strftime("%d.%m.%Y"))