a = 0
b = 0
n = 0
def to_dec(n):
    """Перевод из 10-ичной в 2-ичную систему"""
    a = str(n)[::-1]
    count = 0
    re = 0
    while count < len(a):
        re += int(a[count])*(2**count)
        count += 1
    return re

def to_bin(n):
    """Перевод из 2-ичной в 10-ичную систему"""
    number = ''
    while n != 0:
        number += str(n % 2)
        n = n // 2
    number= number[::-1]
    return number

def to_six(n):
    """Перевод из 10-ичной в 16-ичную систему"""
    number = ''
    remainders = '0123456789ABCDEF'
    while n != 0:
        number += remainders[n % 16]
        n = n // 16
    return number[::-1]

def to_dec_from_six(n):
    """Перевод числа n из 16-ичной в 10-ичную систему"""
    remainders = '0123456789ABCDEF'
    number = n[::-1]
    count = 0
    re = 0
    while count < len(n):
        re += (remainders.index(number[count]) * (16**count))
        count += 1
    return re

def valid_16(n):
    """Проверка правильности ввода числа в шестнадцатиричной системе исчисления"""
    remainders = '0123456789ABCDEF'
    for letter in n:
        if letter in remainders:
            continue
        else:
            return None
    return n

def valid_bin(n):
    """Проверка правильности ввода числа в шестнадцатиричной системе исчисления"""
    numbers_for_bin = '01'
    for letter in str(n):
        if letter in numbers_for_bin:
            continue
        else:
            return None
    return n

def per():
    """ Функция проверяет валидность введенных  данных"""
    while True:
        global a,b,n
        remainders = '0123456789ABCDEF'
        try:
            a = int(input('Выберите сисему исчисления исходного числа\n'
                      'Для двоичной системы - 2 \n'
                      'Для десятичной системы - 10 \n'
                      'Для шестнадцитиричной - 16 \n'
                       ' '))
            if a != 2 and a != 10 and a != 16:                                  # Проверка правильности ввода системы исчисления исходного числа
                print('Введите одну из перечисленных систем исчисления')
                print('===========')
                continue
            else:
                b = int(input('В какую систему исчисления необходимо перевести: '))     # Проверка правильности ввода системы для получения результата
                if a == b:
                    continue
                if  b == 2 or b == 10 or b == 16:
                    if a == 2:
                        try:
                            n = input('Введите исходное число: ')
                            if valid_bin(n) == None:                            # Проверка правильности введения числа в 2-ичной системе
                                continue
                            else:
                                return a,b,n
                        except ValueError:
                            print('Введите число в двоичной системе исчисления')
                            continue
                    if a == 10:
                        try:
                            n = int(input('Введите исходное число: '))          # Проверка что введено число
                            return a,b,n
                        except ValueError:
                            print('Введите число в десятичной системе исчисления')
                            continue
                    else:
                        n = input('Введите исходное число: ')
                        if valid_16(n) == None:                                 # Проверка правильности введения числа в 16-ричной системе
                            continue
                        else:
                            return a,b,n
                else:
                    print('Введите одну из перечисленных систем исчисления')
                    print('===========')
                    continue
            return a,b,n
        except ValueError:
            print('Введите одну из перечисленных систем исчисления')
            print('===========')
            continue