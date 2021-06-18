duration = int(input('Введите промежуток времени в сек - '))
s = duration % 60
# до часа
if 60 < duration < 3600:
    m = duration // 60
    print(m, 'мин', s, 'сек')
# до суток
elif 3600 <= duration < 86400:
    h = duration // 3600
    m = ((duration // 60) % 60)
    print(h, 'час', m, 'мин', s, 'сек')
# в остальных случаях
elif duration >= 86400:
    m = ((duration // 60) % 60)
    h = ((duration // 3600) % 24)
    d = duration // 86400
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
# до минуты
else:
    print(duration, 'сек')
