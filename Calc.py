banner= '''
 ____________________________________________________
|                                                    |
|   [--] Name: Calc Plus                             |
|                                                    |
|   [--] Author: Oleksenko Ivan                      |
|                                                    |
|   [--] Version: ∞ ∞                                |
|____________________________________________________|
'''




print(banner)

def calc():
    global Num_1
    try:  
        Num_1 = float(input('Напиши число\n> '))
    except:
        calc()
    calc2()
    
def calc2():
    act = input('Что нужно сделать? \n1. Сложить \n2. Отнять \n3. Умножить \n4. Поделить \n5. Взвести в степень \n6. Извлечь корень \n0. Перезапуск \n>')
    
    if act == '0':
        calc()
    elif act >= '7':
        calc2()
    try:  
        Num_2 = float(input('Напиши второе число\n> '))
    except:
        calc2()

    if act == '1':
        print('Ответ: ', Num_1 + Num_2) 
    elif act == '2':
        print('Ответ: ', Num_1 - Num_2)
    elif act == '3':
        print('Ответ: ', Num_1 * Num_2) 
    elif act == '4':
        print('Ответ: ', Num_1 / Num_2)
    elif act == '5':
        print('Ответ: ', Num_1 ** Num_2)     
    elif act == '6':
        print('Ответ: ', Num_1 // Num_2)
    else:  
        print('Ты долбоеб?, я дал тебе все возможные варианты ответа, а ты ввел какуе-то хуйню') 
    calc() 
if __name__ == '__main__':
    while True:
     calc()
#Author: IPOleksenko
