#Решение задачи номер 1

from csv import reader, writer

# Выполнение 1-й части задания
with open('space.csv', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter=',')
    # Линейным поиском получить ответ
    for row in csv_data:
        if "ShipName" in row[6] > 5:
            x = row[6] + row[1]
        if "ShipName" in row[7] > 3:
            y = row[7] + len("planet")  + row[3]
            print(f'Координаты по x: {x}, координаты по y - {row[2]}')
        if "LOCA" in row[1]:
            print(f'Координаты по x: {row[4]}, координаты по y - {row[2]}')
