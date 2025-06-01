
#1
"""
Создать класс с двумя переменными.
Добавить метод вывода на экран и метод изменения этих переменных. 
Добавить метод, который находит сумму значений этих переменных,
и метод который находит наибольшее значение из этих двух переменных
"""

class Chisla:

    def __init__(self, first_var, second_var):

        self.first_var = first_var
        self.second_var = second_var
    
    def output_to_scren(self):
        """
        Метод для вывода значений на экран
        """    
        print(f"Переменная 1: {self.first_var}")
        print(f"Переменная 2: {self.second_var}")

    def changing_var(self, new_first_var, new_second_var):
        """
        метод изменения значений
        """
        self.first_var = new_first_var
        self.second_var = new_second_var
    def sum_var(self):
        """
        Метод для нахождения суммы переменных
        """
        return self.first_var + self.second_var
    
    def max_var(self):
        """
        Метод для нахождения наиболщего занчения из двух переменных
        """
        return max(self.first_var,self.second_var)

#2
"""
Описать класс, реализующий десятичный счетчик,
который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне.
Предусмот-реть инициализацию счетчика значениями по умолчанию и произвольными значения-ми.
Счетчик имеет два метода: увеличения и уменьшения, — и свойство,
позволяю-щее получить его текущее состояние. Написать программу,
демонстрирующую все воз-можности класса
"""

class Counter:
    def __init__(self, min_v=0,max_v=10,current_v=None):
        """
        min_v : минимальное значение счетчика (по умолчанию 0)
        max_v : максимальное значение счетчика (по умолчанию 10 )
        current_v :текущее значение счетчика
        """
        self.min_v = min_v
        self.max_v = max_v

        if current_v is None:   #Если текущее значение не задано то мы устанавливаем его как нижняя граница
            self.current_v = min_v
        else:
            if min_v <= current_v <= max_v:     #идет проверка на попадания в промежуток
                self.current_v = current_v
            else:
                raise ValueError("Текущее знчение должно попадать в промежуток [min_v , max_v]")
    def addition_of_one(self):
        """
        Увеличивает значение счетчика на единицу
        """
        if self.current_v < self.max_v:
            self.current_v += 1
        else:
            print("Текущее значение достигло максимального значения")
    def subtraction_of_one(self):
        """
        уменьшает значение счетчика на единицу
        """
        if self.current_v > self.min_v:
            self.current_v -= 1
        else:
            print("Текущее значение достигло минимального значения")
    @property
    def value(self):
        """
        Возвращает текущее значение
        """
        return self.current_v
    def __str__(self):
        """
        возвращает строковое представление счетчика
        """
        return f"Текущее значение счетчика :{self.current_v} ( Диапазон : [{self.min_v},{self.max_v}])"

#3
"""
Составить описание класса многочленов от одной переменной,
задаваемых сте¬пенью многочлена и массивом коэффициентов. 
Предусмотреть методы для вы¬числения значения многочлена для заданного аргумента,
операции сложения, вычитания и умножения многочленов с получением нового объекта-многочлена
"""


class Polynomials:

    def __init__(self , coeff):
        

        """
        инициализирует многочлен.
        coeff:список коэффицентов пример [1,2,3] соответствует 1+2*x + 3*x**2

        """
        self.coeff = coeff
        self.degree = len(coeff) - 1 #степень многочлена.
    
    def meaning_coef(self, x):
        """
        вычисляет значение многочлена и возвращает его
        x :значение аргумента
        """
        result = 0
        for i ,coef in enumerate(self.coeff):
            result += coef *(x**i)
        return result
    
    def __add__(self, other):
        """
        суммирует два многочлена и возвращает новый многчлен
        other : второй многочлен

        """
        if not isinstance(other, Polynomials):
            raise TypeError(" Можно складывать только обьекты класса Polynomials")

        max_len = max(len(self.coeff), len(other.coeff))
        new_coeff = [0] * max_len
        for i in range (len(self.coeff)):   #добовляем коэфиценты из первого многочлена
            new_coeff[i] += self.coeff[i]
        for i in range (len(other.coeff)):  #добовляем коэффиценты из второго многочлена
            new_coeff[i] += other.coeff[i]
        return Polynomials(new_coeff)
    
    def __sub__(self, other):
        """
        Вычитает из одного многочлена другой и возвращает новый многочлен
        other : второй многочлен
        """
        if not isinstance(other, Polynomials):
            raise TypeError(" Можно вычитать только обьекты класса Polynomials")

        max_len = max(len(self.coeff), len(other.coeff))
        new_coeff = [0] * max_len
        for i in range (len(self.coeff)):   #добовляем коэфиценты из первого многочлена
            new_coeff[i] += self.coeff[i]
        for i in range (len(other.coeff)):  #вычитаем коэффиценты 
            new_coeff[i] -= other.coeff[i]
        return Polynomials(new_coeff)

    def __mul__(self, other):
        """
        умножает два ногочлена и возвращает новый многочлен
        other : второй многочлен
        """
        if not isinstance(other, Polynomials):
            raise TypeError(" Можно перемножать только обьекты класса Polynomials")
        
        #находим степень нового многочлена
        new_degree = self.degree + other.degree
        new_coeff = [0] * (new_degree +1)

        for i in range(len(self.coeff)):
            for j in range (len(other.coeff)):
                new_coeff[i+j] +=self.coeff[i] * other.coeff[j]
        return Polynomials(new_coeff)
    
    def __str__(self):
        """
        возвращает сттрокове представление многочлена
        """
        k=[]

        for i ,coef in enumerate(self.coeff):
            if coef == 0:
                continue
            if i == 0 :
                k.append(f"{coef}")
            elif i ==1 :
                k.append(f"{coef}x")
            else:
                k.append(f"{coef}x^{i}")
        return "+".join(k[::-1]) if k else "0"  

if __name__ == "__main__":


    #1
    obj = Chisla(10, 20) #создаем обьеrn класса

    #вывод значений
    print("изначальные значения переменных")
    obj.output_to_scren()

    #вывод суммы переменныз
    print(f"Сумма переменных: {obj.sum_var()}")

    #вывод наибольшего значения
    print(f"Наибольшее значение: {obj.max_var()}")



    #смена занчений переменных
    obj.changing_var(30,8)

    #вывод новых значений
    print("обновленные значения переменных")
    obj.output_to_scren()

    #вывод суммы новых переменных
    print(f"Сумма переменных: {obj.sum_var()}")

    #вывод нового наибольшего значения
    print(f"Наибольшее значение: {obj.max_var()}")



    #2

    counter1 = Counter() #Создаем счетчик с значениями по умолчанию (min_v=0, max_v=10,current_v = 0)
    print(counter1)

    #увеличиваем счетчик на три единицы

    counter1.addition_of_one()
    counter1.addition_of_one()
    counter1.addition_of_one()
    print(counter1)

    #теперь уменьшим счетчик на один 
    counter1.subtraction_of_one()
    print(counter1)

    #Теперь попробуем выйти за верхнюю и нижнюю границу
    for _ in range(11):
        counter1.addition_of_one()
    print(counter1)

    for _ in range(11):
        counter1.subtraction_of_one()
    print(counter1)

    #Задаем новые граицы для счетчика
    counter2=Counter(min_v=5,max_v=15,current_v=10)
    print("\nСчетчик 2 :")
    print(counter2)

    #повторяем операции
    counter2.addition_of_one()
    counter2.addition_of_one()
    print(counter2)

    counter2.subtraction_of_one()
    print(counter2)


    #3
    #создаем многочлены
    p1= Polynomials([1,2,3])
    p2= Polynomials([4,5])

    #выводим многочлены
    print(f"Многочлен p1: {p1}")
    print(f"Многочлен p2: {p2}")
    
    #вычисляем значсение многочлена p1 при x=3
    x =3
    print(f"Значение p1 при x = {x}: {p1.meaning_coef(x)}")

    #сложение многочленов
    p_sum= p1 +p2
    print(f"Сумма p1 и p2: {p_sum}")
    
    #Вычитание многочленов
    p_dif= p1 - p2
    print(f"Разность p1 и p2: {p_dif}")

    #Умножение многочленов
    p_prod= p1 * p2
    print(f"произведение p1 и p2: {p_prod}")