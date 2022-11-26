ex_num = int(input('Введите номер задания (от 1 до 5): ' ))
if ex_num == 1:
    weekdays = {}
    
    for i in range(1,6):
        weekdays[i] = 'будний день'
    
    weekdays[6] = weekdays[7] = 'выходной день'
    try:
        day = int(input('Введите номер дня недели: '))
        if 1 <= day <= 7:
            print(weekdays[day])
        else:
            print('Вы ввели какую-то дичь')
    except:
        day=-1
        print('Вы ввели какую-то дичь')
    
elif ex_num == 2:

    for x in range(2):
        for y in range(2):
            for z in range(2):
                sentence = not (x or y or z) == ((not x) and (not y) and (not z))
                if sentence:
                    print(f'При x = {x}, y = {y} и z = {z} выражение истинно')
                else:
                    print(f'При x = {x}, y = {y} и z = {z} выражение ложно')

elif ex_num == 3:
    try:
        x, y = (float(i) for i in input('Введите координаты точки X и Y через пробел: ').split())
        if x > 0:
            if y > 0:
                print('Точка находится в I четверти')
            elif y < 0:
                print('Точка находится в IV четверти')
            else:
                print('Точка находится на оси Y')
        elif x < 0:
            if y > 0:
                print('Точка находится в II четверти')
            elif y < 0:
                print('Точка находится в III четверти')
            else:
                print('Точка находится на оси Y')
        else:
            print('Точка находится на оси X')
    except:
        print('Вы ввели какую-то дичь')

elif ex_num == 4:
    try:
        quarter_num = int(input('Введите номер четверти координатной плоскости: '))
        if quarter_num == 1:
            print('X: (0;+inf)')
            print('Y: (0;+inf)')
        elif quarter_num == 2:
            print('X: (-inf;0)')
            print('Y: (0;+inf)')
        elif quarter_num == 3:
            print('X: (-inf;0)')
            print('Y: (-inf;0)')
        elif quarter_num == 4:
            print('X: (0;+inf)')
            print('Y: (-inf;0)')
        else:
            print('Вы снова ввели какую-то дичь!')
    except:
        print('Вы снова ввели какую-то дичь!')

elif ex_num == 5:
    try:
        a = [float(i) for i in input('Введите координаты точки A в формате: (0,0)')[1:-1].split(',')]
        b = [float(i) for i in input('Введите координаты точки B в формате: (0,0)')[1:-1].split(',')]  
        d = 0
        for i,j in zip(a,b):
            d += (i-j)**2
        print(f'Расстояние между точками A и B равно {d**.5}')
    except:
        print('Вы начинаете выводить меня из себя!')