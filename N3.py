#Отсортируйте словарь по значению в порядке возрастания и убывания
dictionary = { 51:2, 99:1, 8:25, 20:5, 5:32}
sort= {}
sort_key = sorted(dictionary, key=dictionary.get)
for i in sort_key:
    sort[i] = dictionary[i]
print(sort)