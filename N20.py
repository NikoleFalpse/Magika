#С помощью анонимной функции извлеките из списка числа, делимые на 15.
numbers=list(map(int, input("Введите числа через пробел: ").split(" ")))
new_num = list(filter(lambda x: (x%15 == 0) , numbers))
print(new_num)