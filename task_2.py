'''
2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Примеры/Тесты:
4 4 -> 2 2
5 6 -> 2 3
Примечание.
Вариант 1. Здесь нужно составить два уравнения. Которые приведут к квадратному уравнению.
Кто не помнит, как решать квадратное уравнение - посмотрите в сети. Обойдите дополнительной проверкой возможность комплексных 
решений. Можно игнорировать то, что получаться рациональные решения вместо натуральных.
Для вычисления квадратного корня используйте возведение в степень 0.5 или
(*) Усложнение для варианта 1. найдите самостоятельно в сети какая функция стандартной библиотеки вычисляет квадратный корень и как до нее добраться.
Вариант 2. Решить эту задачу можно "перебором значений" в цикле

!!! Комментарий к решению. !!!
Если дискриминант меньше нуля, то корней у квадратного уравнения нет, то есть не существует двух чисел, сумма которых равна 
S и произведение которых равно P. Если дискриминант больше нуля, то есть есть два корня у квадратного уравнения, 
но они могут быть не целыми числами, либо не удовлетворять условиям задачи. 
Например, если S = 5, P = 6, то корни уравнения будут x1 = 3 и x2 = 2, но только x1 и y1 = 2 удовлетворяют условиям, 
а x2 и y2 = 3/2 - нет. Поэтому нужно проверять каждый корень на соответствие условиям.
'''

# Вариант 1:
print("\033[1mВариант 1 - перебор значений в цикле.\033[0m")

while True:
    try:
        summa = int(input("\033[32mВведите первую подсказку от Пети - сумму чисел: \033[0m"))        
        break
    except ValueError:
        print("\033[31mОшибка! Введено не число.\033[0m")
while True:
    try:
        mult = int(input("\033[32mВведите вторую подсказку от Пети - произведение чисел: \033[0m"))
        break
    except ValueError:
        print("\033[31mОшибка! Введено не число.\033[0m")
# Ищем два числа X и Y, удовлетворяющих условиям X + Y = summa и X * Y = mult 
# с проверкой Х!=0 и что произведение Х и Y действительно равно заданному значению
for x in range(-summa, summa+1):
    if x != 0 and mult % x == 0:
        y = mult // x
        if x + y == summa and x * y == mult:
            print("\033[34mЗадуманные Катей числа: {} и {}.\033[0m".format(int(x), int(y)))
            break
else: 
    print("\033[33mПодсказки Пети неверные, числа не найдены.\033[0m")


# Вариант 2:
print("\033[1mВариант 2 - через квадратное уравнение.\033[0m")
# Для работы с модулем стандартных математических функций math, его необходимо импортировать. 
import math

while True:
    try:
        summ = int(input("\033[32mВведите первую подсказку от Пети - сумму чисел: \033[0m"))        
        break
    except ValueError:
        print("\033[31mОшибка! Введено не число.\033[0m")
while True:
    try:
        multi = int(input("\033[32mВведите вторую подсказку от Пети - произведение чисел: \033[0m"))
        break
    except ValueError:
        print("\033[31mОшибка! Введено не число.\033[0m")
# Ищем два числа a и b, удовлетворяющих условиям a + b = summ и a * b = multi
disc = summ*summ - 4*multi # дискриминант квадратного уравнения
# Проверяем, есть ли корни у квадратного уравнения
if disc < 0:
    print("\033[33mПодсказки Пети неверные, числа не найдены.\033[0m")
elif disc == 0:
    a = b = summ/2
    if a.is_integer() and b.is_integer() and a*b == multi:
        print("\033[34mЗадуманные Катей числа: {} и {}.\033[0m".format(int(a), int(b)))
    else:
        print("\033[33mПодсказки Пети неверные, числа не найдены.\033[0m")
else:
    # Вычисляем корни уравнения
    a1 = (summ + math.sqrt(disc))/2
    a2 = (summ - math.sqrt(disc))/2
    # Проверяем каждый корень на соответствие условиям
    if a1.is_integer():
        b1 = multi/a1
        if b1.is_integer() and a1 + b1 == summ:            
            print("\033[34mЗадуманные Катей числа: {} и {}.\033[0m".format(int(a1), int(b1)))
            exit()
    if a2.is_integer():
        b2 = multi/a2
        if b2.is_integer() and a2 + b2 == summ:
            print("\033[34mЗадуманные Катей числа: {} и {}.\033[0m".format(int(a2), int(b2)))
            exit()
    print("\033[33mПодсказки Пети неверные, числа не найдены.\033[0m")
