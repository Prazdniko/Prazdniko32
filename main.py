#Решение задачи номер 3

from csv import reader

group_data = 0
with open('space.csv', encoding='utf-8') as data_file:
    # Открыть файл с данными как объект reader
    csv_data = reader(data_file, delimiter=',')
    # Линейным поиском получить ответ:
    group_data = input('Введи название карабля или в введите STOP: ')
    while group_data != 'STOP':
        group_data = input('Введи название карабля или в введите STOP: ')
        print('Корабль',<ShipName>,'был отправлен с планеты:',<planet>,'и его направление движения было:,'<direction>)
    else:
        print('error.. er.. ror..')
        break