'''Напишите программу,
 которая выводит чётные числа из заданного списка и останавливается, 
если встречает число 237'''
numbers=input("Введите числа через пробел: ").split(" ")
numbers=list(map(int, numbers))
for i in numbers:
    if i%2==0:
        print(i)
    if i==237:
        break