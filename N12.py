#программа принимает имя файла и выводит его расширение.
from os import path
import tkinter as tk
import tkinter.filedialog as fd
filename = fd.askopenfilename(title="Открыть файл", initialdir="/")
file_type= path.splitext(filename)
print("Расширение файла: ",file_type[1])