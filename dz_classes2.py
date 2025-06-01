
import math
#1
"""
Создать абстрактный класс Figure (на плоскости) с методами вычисления пло-щади и периметра,
а также методом, выводящим информацию о фигуре на экран.
Создать подклассы: Rectangle (прямоугольник), Circle (круг), Triangle (треугольник) со своими методами вычисления площади и периметра.
Создать список из n фигур и вывести полную информацию о фигурах на экран.

"""
class Figure:      
    def area(self):
        """
        метод для вычисление площади (он должен быть переопределен в подклассах)
        """
        raise NotImplementedError("Метод area()должен быть переопределен в подклассах")
    
    def perimeter(self):
        """
        метод длф вычисление периметра (он должен быть переопределен в подклассах)
        """
        raise NotImplementedError("Метод perimeter()должен быть переопределен в подклассах")
    
    def display_info(self):
        """
        метод для вывода информации о фигуре (он должен быть переопределен в подклассах)
        """
        raise NotImplementedError("Метод perimeter()должен быть переопределен в подклассах")
    
class Rectangle(Figure):        #подкласс Rectangle(прямоугольник)
    def __init__(self,width,heigth):
        self.width = width
        self.heigth = heigth
    
    def area(self):
        return self.width * self.heigth
    
    def perimeter(self):
        return 2 * (self.width + self.heigth)
    
    def display_info(self):
        print(f" Прямоугольник : ширина = {self.width}, высота = {self.heigth}")
        print(f" Площадь  : {self.area()}")
        print(f" Периметр : {self.perimeter()}")
        print()     # для промежутка

class Circle(Figure):       #подкласс Circle(круг)
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 
    
    def perimeter(self):
        return  2 * math.pi * self.radius
    
    def display_info(self):
        print(f" Круг    : радиус = {self.radius}")
        print(f" Площадь : {self.area()}")
        print(f" Периметр (длина окружности): {self.perimeter()}")
        print()     # для промежутка

class Triangle(Figure):         #подкласс Triangle(треугольник)
    def __init__(self,side1, side2 ,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        #Формула Герона
        s =self.perimeter() / 2
        return math.sqrt(s* (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def display_info(self):
        print(f" Треугольник : стороны = {self.side1},{self.side2},{self.side3},")
        print(f" Площадь  : {self.area()}")
        print(f" Периметр : {self.perimeter()}")
        print()     # для промежутка


#2
"""
Составить описание класса для вектора,
заданного координатами его концов в трехмерном пространстве.
Реализовать операции сложения и вычитания векто-ров, 
результатом которого является вектор,
а также вычисления скалярно-го произведения двух векторов,
длины вектора, косинуса угла между двумя век-торами.

"""


class Vector:
    def __init__(self,x1,y1,z1,x2,y2,z2):
        """
        инициализирает координаты вектора
        x1,y1,z1 :коодинаты начала вектора
        x2,y2,z2 :координаты конца вектора
        """
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2 
        self.z2 =z2 

    def coord(self):
        """
        находит координаты вектора и возвращает их кортежом
        """
        return ( self.x2 - self.x1, self.y2 -self.y1 , self.z2 - self.z1)
    
    def __add__(self,other):
        """
        сложение двух векторов
        other : другой вектор
        """
        x1,y1,z1 = self.coord()
        x2,y2,z2 = other.coord()
        return Vector(0,0,0,x1+x2,y1+y2,z1+z2)
    def __sub__(self,other):
        """
        вычитание двух векторов
        other : другой вектор
        """
        x1,y1,z1 = self.coord()
        x2,y2,z2 = other.coord()
        return Vector(0,0,0,x1-x2,y1-y2,z1-z2)
    
    def scalar_product(self,other):
        """
        вычисляется скалярное произведение двух векторов
        other : другой вектор
        """
        x1,y1,z1 = self.coord()
        x2,y2,z2 = other.coord()
        return x1*x2+y1*y2+z1*z2
    def lengtV(self):
        """
        вычисление длины вектора

        """
        x,y,z = self.coord()
        return math.sqrt(x**2+y**2+z**2)
    
    def cosV(self,other):
        """
        нахождение косинуса угла между двумя векторами
        other : другой вектор
        """
        scal=self.scalar_product(other)
        len1=self.lengtV()
        len2=other.lengtV()
        return scal/(len1+len2)

    def __str__(self):
        """
        возвращаем строковое представление вектора
        """
        x,y,z = self.coord()
        return f"вектор : ({x},{y},{z})"


if __name__ == "__main__":
    
    #1
    figures = [ Rectangle(5, 10), Circle(7), Triangle(3, 4, 5), Rectangle(8, 6), Circle(10), Triangle(5, 12, 13)]
    for figure in figures:
        figure.display_info()

    #2

    vect1 = Vector(0,0,0,1,2,3)
    vect2 = Vector(0,0,0,3,4,5)

    print("вектор 1 :",vect1)
    print("вектор 2 :",vect2)

    #сложение векторов

    vect3 = vect1 +vect2
    print("сумма векторов  :",vect3) 

    #вычитание векторов   
    vect3 = vect1 -vect2
    print("разность векторов  :",vect3) 

    #скаярное произведение
    scal = vect1.scalar_product(vect2)
    print("скаляное произведение :",scal)

    #длина вектора
    len1 = vect1.lengtV
    len2 = vect2.lengtV
    print("длина вектора 1 :",len1)
    print("длина вектора 2 :",len2)

    #косинус угла между векторами
    cos =vect1.cosV(vect2)
    print("Косинус угла меду векторами",cos)