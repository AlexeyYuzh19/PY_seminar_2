'''
2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
Примеры/Тесты:
10 ->
1
2
4
8
(*) Усложнение. Вывод оформить в одну строку: числа выводить через запятую. Для этого воспользоваться параметрами функции print
Примеры/Тесты:
10     -> 1,2,4,8,
10000  -> 1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,
'''

# Вариант 1:
print("\nВариант 1")
while True: 
    try: 
        value = int(input("\033[1m\033[35mВведите целое положительное число больше 0 : \033[0m")) 
        if value <= 0: 
            print("\033[31mОшибка! Значение должно быть больше нуля.\033[0m") 
            continue 
        break 
    except ValueError: 
        print("\033[31mОшибка! Введите целое число больше 0.\033[0m")
print(f"Все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа {value} :")
pow = 0 
search = 2**pow
while search <= value:
    com = "," if search <= (value - search) else ".\n"    
    print(f"{search}{com}", end=" ")
    pow += 1 
    search = 2 ** pow

# Вариант 2:
print("\nВариант 2")
while True: 
    try: 
        num = int(input("\033[1m\033[35mВведите целое положительное число больше 0 : \033[0m")) 
        if num <= 0: 
            print("\033[31mОшибка! Значение должно быть больше нуля.\033[0m") 
            continue 
        break 
    except ValueError: 
        print("\033[31mОшибка! Введите целое число больше 0.\033[0m") 
# список с кодами ANSI-цветов для чередования 
colors = ["\033[31m", "\033[32m", "\033[33m", "\033[34m"] 
# итерируемся по степеням двойки от 0 до log2(num) 
print(f"Все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа {num} :") 
for k in range(num.bit_length()): 
    # вычисляем текущую степень двойки 
    power = 2 ** k 
    # если текущая степень двойки не превышает N, выводим ее 
    if power <= num: 
        # определяем, какой цвет использовать для текущего значения 
        colIn = k % len(colors) 
        # выводим значение с соответствующим цветом и запятой или точкой 
        com = "," if power <= (num - power) else "."
        print(f"{colors[colIn]}{power}\033[0m{com} ", end=" ")

# Вариант 3:
print("\nВариант 3")

while True: 
    try: 
        set = float(input("\033[32mВведите положительное число \033[1mне менее\033[0m\033[35m 0,00001 : \033[0m")) 
        if set < 0.00001: 
            print("\033[31mОшибка! Значение должно быть \033[1mболeе\033[0m\033[35m 0,00001.\033[0m") 
            continue 
        break 
    except ValueError: 
        print("\033[31mОшибка! Введите число.\033[0m")
degre = -16
num = 2 ** degre
if num <= set:
    print("\033[47m\033[36m\033[1mВсе целые степени двойки, от значения {} до числа {} :\033[0m".format("0,00001", set))
    while num <= set:
        if num < 1:        
            print("\033[47m\033[35m{:13.6f}  [ 2 в степени {:3.0f} ]   \033[0m".format(num, degre))
        else:
            print("\033[47m\033[36m{:13.0f}  [ 2 в степени {:3.0f} ]   \033[0m".format(num, degre))
        degre += 1
        num = 2 ** degre
else:
    print(f"\033[47m\033[33m\033[1mВ диапазоне от 0,00001 отсутствуют степени двойки, не превосходящие числа {set}.\033[0m")
    
# Вариант 4:
print("\nВариант 4 - алгоритм варианта 3, изменен вывод в консоли")
const1 = 0.00001
while True: 
    try: 
        set1 = float(input("\033[32mВведите положительное число \033[1mне менее\033[0m\033[35m {:.5f} : \033[0m".format(const1))) 
        if set1 < const1: 
            print("\033[31mОшибка! Значение должно быть \033[1mболeе\033[0m\033[35m {:.5f}.\033[0m".format(const1)) 
            continue 
        break 
    except ValueError: 
        print("\033[31mОшибка! Введите число.\033[0m")
degre1 = -16
num1 = 2 ** degre1
if num1 <= set1:
    print("\033[47m\033[36m*\033[0m"*62 + "\n\033[47m\033[36m\033[1m Все целые степени двойки, от значения {:.5f} до числа {} : \033[0m".format(const1, set1))    
    value1 = "значение возведения в степень числа 2"
    value2 = "значение степени" 
    print("\033[47m\033[36m*\033[0m"*62 + "\n\033[47m\033[36m" + value1.center(40) + "|" + value2.center(21) + "\033[0m\n" + "\033[47m\033[36m-\033[0m"*62)           
    while num1 <= set1:
        if num1 < 1:        
            print("\033[47m\033[35m{:38.6f}  |{:^17.0f}\033[0m".format(num1, degre1))
        else:
            print("\033[47m\033[36m{:38.0f}  |{:^17.0f}\033[0m".format(num1, degre1))
        degre1 += 1
        num1 = 2 ** degre1
    print("\033[47m\033[36m-\033[0m"*58) 
else:
    print("\033[47m\033[33m\033[1mВ диапазоне от {:.5f} отсутствуют степени двойки, не превосходящие числа {:.7f}.\033[0m".format(const1, set1))