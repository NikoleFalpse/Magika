#Найдите три ключа с самыми высокими значениями в словаре 
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sort_dict=dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(sort_dict)
k=list(sort_dict.keys())
for i in range(3):
    print(k[i])
