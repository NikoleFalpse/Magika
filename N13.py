#При заданном целом числе n посчитайте n + nn + nnn
def v(n):
    res=n+n*n+n*n*n
    print(res)
n=input("Введите любое число: ")
if '.' in n:
    n=float(n)
else:
    n=int(n)
if isinstance (n, int)==True:
    v(n)
else:
    print("Error")
