#Посчитайте, сколько раз символ встречается в строке
a=input("Введите строку: ")
check=0
for i in a:
    if i==',':
        check+=1
print("В строке символ , содержится ",check," раз(а)")
