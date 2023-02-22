#7) Узнайте, какой был 7-го января 2015 года
from datetime import datetime

date = datetime(year=2015, month=1, day=7)
print(date.strftime("%A"))