#Домашнее задание по теме "Режимы открытия файлов"
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        text_file = file.read()
        file.close
        return(text_file)
    def add(self, *products):
        for Name_Product in products:
            _products = self.get_products()
            if Name_Product.name in _products:
                print(f'Продукт {Name_Product.name} уже есть в магазине')
            else:
                _file = open(self.__file_name, 'a')
                _file.write(f'{Name_Product}\n')
                _file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
