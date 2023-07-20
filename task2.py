'''Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
'''

class Archive:
    '''класс запоминает ранее введенную информацию
    '''
    _instance = None
    _archive = []
    def __new__(cls, name: str, age: int):
        ''' При создании нового экземпляра класса значения атрибута предыдущего
            экземпляра сразу помещаются в архив '''
        instance = super().__new__(cls)
        if cls._instance is not None:
            cls._archive.append(cls._instance)  
        cls._instance = instance
        instance.archive = cls._archive.copy()
        return cls._instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'

    def __str__(self):
        return f"Игрок {self.name}. До него играли {[pl.name for pl in self.archive]}"

p1 = Archive("Трина", 45)  
p2 = Archive("Рина", 40) 
p3 = Archive("Кир", 35)           
print(p1)
print(p1.archive)
print(p2)
print(p2.archive)
print(p3)
print(p3.archive)
print(f"Документация метода создания объекта - >  {Archive.__new__.__doc__}")
#help(Archive)