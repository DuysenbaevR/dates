#10) Выведите на экран количество секунд,
# которое осталось до конца дня.

hour = int(input('Sagatti kiritin: '))
min = int(input('Minutti kiritin: '))
print(f"Kun aqirina deyin {(23-hour)*3600 + (60-min)*60} sekund qaldi")