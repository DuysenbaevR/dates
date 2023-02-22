#14) Написать скрипт: Определение количества времени,
# которое прошло между двумя датами
from datetime import datetime

first_data = datetime(year=2023, month=5, day=15)
second_data = datetime(year=2018, month=9, day=24)

delta = first_data - second_data
print(f"arasindagi pariq {delta} ")