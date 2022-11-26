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

    
    
    
    
    
    

    
    
    
    
    
    
    
    
except:
    print('Недопустимый номер задачи. Попробуйте еще раз')
