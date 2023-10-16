#Выведите список файлов в указанной директории.
import os
from tkinter import filedialog
import tkinter
direct = filedialog.askdirectory()
#folder_path.set(direct)
spisiok=os.listdir(direct)
for i in spisiok:
    print(i)