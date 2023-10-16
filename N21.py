#Нужно проверить, все ли числа в последовательности уникальны.
from random import randint
a=[]
for i in range(5):
    a.append(randint(0,10))
print(a)
seta = set(a)
if len(a) == len(seta):
    print("Все числа уникальны")
else:
    print("Есть одинаковые")
