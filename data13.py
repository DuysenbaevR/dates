#13) Есть дата например 31.12.2013.
# Реализуйте средствами языка Python скрипт,
# который будет вычислять сколько осталось дней, месяцев, лет до этой даты.
from datetime import datetime

date = datetime.now()

given_data = datetime(year=2045, month=12, day=31)

delta = given_data - date

print(f"{delta.days} kun qaldi")