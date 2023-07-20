'''Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''
import datetime
class MyString(str):
    ''' Класс , кроме строки, хранит еще имя автора и время содания '''
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance
    
    def __repr__(self):
        return f"Строка {self} автор {self.name} , время создания {self.date}"
    
      

str_1 = MyString("ХОРОШОТОХОРОШО", "Serg")
print(str_1.date)
print(str_1)
print(repr(str_1))
print(f'Документация класса: {MyString.__doc__ }')

    