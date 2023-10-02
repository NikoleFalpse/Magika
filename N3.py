#Отсортируйте словарь по значению в порядке возрастания и убывания
dictionary = { 51:2, 99:1, 8:25, 20:5, 5:32}
sort= {}
sort = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(sort)
sort = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
print(sort)