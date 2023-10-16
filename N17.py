#Сложите цифры целого числа
a =input("Введите целое число: ")
sum=0
if '.' not in a:
    a=int(a)
    while a > 0:
        puth = a % 10
        sum += puth
        a //= 10
    print(sum)
else:
    print('Error')
