try:
    ex_num = int(input('Введите номер задачи: '))
    if ex_num == 1:
        def factorial(x):
            if x > 1:
                return x * factorial (x-1)
            else:
                return 1
        
        try:
            n = int(input('Введите число N: '))
            for i in range(1, n+1):
                print(factorial(i), end=' ')
        except:
            print('Недопустимое значение N. Повторите попытку')
    
    if ex_num == 2:

        try:
            n = int(input('Введите число N: '))
            k = 0

            for i in range(2, n // 2):
                if n % i == 0:
                    k = i
                    print(f'Делитель равен {k}')
                    break
            if not k:
                print(f'Делитель равен {n}')
            
        except:
            print('Вы ввели какую-то дичь')

    if ex_num == 3:
        try:
            n = int(input('Введите число N: '))

            lst = [i for i in range(-n,n+1)]
            print(*lst, sep=' ')
            try:
                indexes = [int(i) for i in input('Введите индексы элементов для произведения через пробел: ').split()]
            except:
                print('Нет, вы не поняли! В следующий раз - введите индексы через пробел')

            production = 1
            errors = []
            for i in indexes:
                try:
                    production *= lst[i]
                except:
                    errors.append(i)
                    continue
            print(f'Произведение элементов равно {production}')
            if errors:
                print('В массиве отсутствуют элементы с индексами:', *errors, sep=' ')

        except:
            print('Ну вот, опять какая-то дичь :(')
    
    if ex_num == 4:

        try:
            n = int(input('Введите натуральное число N: '))
            if n <= 0:
                print('Я же просил ввести НАТУРАЛЬНОЕ число!')
            
            else:
                summary = 0

                for i in range(2, n+1, 2):
                    summary += i
                
                print(f'Сумма четных чисел от 1 до {n} равна {summary}')

        except:
            print('Число, Карл! Введи ЧИСЛО!')
    
except:
    print('Недопустимый номер задачи. Попробуйте еще раз')
