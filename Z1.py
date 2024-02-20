from collections import namedtuple
class Assignment():
    global n_count
    n_count=0
    def __init__(self, name_p, content, date_extradition, f_execution, name_extr):
        self.n_count+=1
        """self.name_p=name_p
        self.content=content
        self.date_extradition=date_extradition
        self.f_execution=f_execution
        self.name_extr=name_extr"""
        assign=dict({"№":n_count, "Название поручения": name_p, "Содержание": content, "Дата выдачи": date_extradition, "Дата факт.исполнения":f_execution, "Кто выдал": name_extr })
  
 #   def New_assignment(self, assign):


ass1=Assignment("Сходить за хлебом", "Закончился хлеб. Сходить за черным зерновым. 2 булки", "15.02.2024", "16.02.2024", "Афанасьев К.Л.")
ass2=Assignment("Ксерокопии", "Сделать ксерокопии отчета для встречи", "15.02.2024", "15.02.2024", "Тирешко П.Р.")
ass3=Assignment("Пропуски", "Сделать пропуски для новеньких стажеров", "16.02.2024", "20.02.2024", "Кириченко И.И.")
ass4=Assignment("Почта", "Рассортировать почту по убыванию", "18.02.2024", "21.02.2024", "Сахарова М.А.")
assign=namedtuple(ass1,ass2,ass3,ass4)
print(assign)
    

