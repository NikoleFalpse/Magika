#вывести треугольник Паскаля
def next_row(row):
    row = [1] + row
    for i in range(1, len(row)-1):
        row[i] += row[i+1]
    return row

row = []
number =int(input("Введите количество строк: "))
for i in range(number):
    row = next_row(row)
    print(row)
        