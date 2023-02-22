#8) Выведите на экран количество часов, прошедшее
# между 1 марта 1988 года и текущим моментом с помощью Date.parse

from datetime import datetime

current_date = datetime.now()

x_date_time = datetime(year=1988, month=3, day=1)

timedelta = current_date - x_date_time

print(f"Hazirge shekem {timedelta.days * 24} sagat otti")