'''
    Рисование графиков
'''
import tkinter as tk
import math 
mainm = tk.Tk()
mainm.title('наше окно')
mainm.geometry('1000x800')



def drawScale(isVertical: int = 1, scale: int = 10, center_x: int = 500, center_y: int = 400,length: int = 500):
    '''
    функция рисует шкалу на оси
        :param isVertical - признак вертикальная ось: 1 или горизонтальная: 0
        :param scale - масштаб
        :param length - длина оси
        :param center_x - x координата центра системы координат
        :param center_x - x координата центра системы координат
     '''
    width = int(canv.__getitem__('width') )  # узнали шириину полотна
    height = int(canv.__getitem__('height') )  # узнали высоту полотна
    
    if isVertical == 0:     # отчсечки на горизонтальной оси
        x_shift = (width-length)//2
        start = center_x - x_shift
        n = (length-start)//scale     # количество отсечек на  положительной части оси x
        m = (start)// scale      # количество отсеек на отрицательной части оси x
        
        for i in range(n):
            canv.create_line(center_x + i*scale, center_y - 5, center_x + i*scale,  center_y + 5)
            #нумерация отсечек на положительной части оси
            canv.create_text(center_x + (i+1)*scale  , center_y + 15, text = str(i+1))

        for i in range(m):
            canv.create_line(center_x - i*scale, center_y - 5, center_x - i*scale,  center_y + 5)  
            #нумерация отсечек отрицательной части оси
            canv.create_text(center_x - (i+1)*scale , center_y + 15, text = str(i+1))

        # промежуточные горизонтальные отсечки
        for i in range(n * 5):
            canv.create_line(center_x + i*(scale/5), center_y - 2, center_x + i*(scale/5),  center_y + 2)
        for i in range(m * 5):
            canv.create_line(center_x - i*(scale/5), center_y - 2, center_x - i*(scale/5),  center_y + 2)  


    else:     # отчсечки на вертикальной оси
        y_shift = (height-length)//2
        start = center_y - y_shift
        n = (length-start)//scale     # количество отсеек на отрицательной части оси y
        m = (start)// scale      # количество отсечек на  положительной части оси y
        for i in range(n):
            canv.create_line(center_x + 5, center_y + i*scale, center_x -5,  center_y + i*scale)
            #нумерация отсечек на  положительной части оси
            canv.create_text(center_x - 15, center_y + (i+1)*scale, text = str(i+1))

        for i in range(m):
            canv.create_line(center_x + 5, center_y - i*scale, center_x -5,  center_y - i*scale)     
            #нумерация отсечек на  отрицательной части оси
            canv.create_text(center_x - 15, center_y - (i+1)*scale, text = str(i+1) )
        
        # промежуточные вертикальные отсечки
        for i in range(n * 5):
            canv.create_line(center_x + 2, center_y + i*(scale/5), center_x - 2,  center_y + i*(scale/5))
        for i in range(m * 5):
            canv.create_line(center_x + 2, center_y - i*(scale/5), center_x - 2,  center_y - i*(scale/5))

def drawAxe(isVertical: int = 1, length: int = 500, isNeededLines: bool = False, width: int = 1000, height: int = 800,center_x: int = 500, center_y: int = 400, scale: int = 10):
    '''
    функция рисует ось координат (горизонтальную или вертикальную)
        
        :param isVertical - признак вертикальная ось: 1 или горизонтальная: 0
        :param length - длина оси
        :isNeededLines - нужна ли шкала на оси
        :param center_x = координата центра координат по x
        :param center_y = координата центра координат по y
        :param scale - масштаб
        :param width: - ширина полотна
        :param height: - высота полотна
    '''
    if isVertical:
        y_shift = (height-length)//2
        canv.create_line(center_x, y_shift, center_x, y_shift + length, arrow = 'first')
        drawScale(1, scale, center_x,center_y, length)
    else:
        x_shift = (width-length)//2
        
        canv.create_line(x_shift, center_y, x_shift + length, center_y, arrow = 'last')
        drawScale(0, scale, center_x, center_y, length)
        
    

def create_dpsk(axesx: int = 1, axesy: int = 1, scale: int = 10, width: int = 1000, height: int = 800, center_x: int = 500, center_y: int = 400):
    '''
        Функция рисует Декартову систему координат на плокости
        :param axesx: - наличие осей координат Оx 0 - нет, 1 -есть 
        :param axesy: - наличие осей координат Оy 0 - нет, 1 -есть 
        :param scale: - масштаб
        :param width: - ширина полотна
        :param height: - высота полотна
        :param center_x = координата центра координат по x
        :param center_y = координата центра координат по y

    '''
    drawAxe(center_x=center_x, center_y=center_y, scale = scale)
    drawAxe(center_x=center_x,center_y=center_y, scale=scale, isVertical=0,length=800)


def f(x):
    '''
        Функция
    '''
    
    return x**2

def graph_func(center_x: int = 500, length: int = 500, height: int = 800 ):
    '''
        Функция показывает используемю функцию
        :param center_x = координата центра координат по x
        :param length - длина оси
        :param height: - высота полотна

    '''
    y_shift = (height-length)//2 

    func_nam = tk.Label(mainm, text = " Это график функции: tan(x)" , bg = "white")
    func_nam.place(x=center_x + 10, y= y_shift)


def draw_func(func, a: int, b: int, scale, center_x, center_y , colour : "black"):
    ''' 
        :param func: 
        :param  a: 
        :param b:
        :param scale: - масштаб
        :param center_x = координата центра координат по x
        :param center_y = координата центра координат по y
        :param colour: - цвет функции (название цвета писать в формате str пример: "green")
    '''
    length = b - a   # длина отрезка
    h = 0.001         # шаг для рисования графика функции
    n = int(length / h)
    for i in range(n-1):
        x0 =  (a+i*h)*scale
        y0 =  func(a+i*h)*scale 
        x1 = (a+(i+1)*h)*scale
        y1 =  func(a+(i+1)*h)*scale 
        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1 , fill=colour)

def designation_of_points(x, func, scale, center_x, center_y, dots_and_dashes: int=1, colour="red"):
    '''
        Функция вычисляет значение функции в заданной точке и отображает ее на графике
        :param x: координата точки x
        :param func: функция значение которой вычисляется
        :param scale: масштаб
        :param center_x: координата центра координат по x
        :param center_y: координата центра по y
        :param dots_and_dashes: признак существования пунктира и точек x,y: 1 или их отсутствия:0
        :param colour: цвет точки
    '''
    y = func(x)
    # Масштабируем коордианты x и y
    x_scaled = x * scale
    y_scaled = y * scale

    # рисуем точку на графике

    canv.create_oval(center_x + x_scaled-3, center_y - y_scaled -3, center_x + x_scaled +3, center_y - y_scaled +3 , fill=colour)   # точка (x;y)
    canv.create_text(center_x +x_scaled +10, center_y - y_scaled -10, text = f"({x:.2f}, {y:.2f})", fill = colour)
    
    if dots_and_dashes:
        canv.create_oval(center_x + x_scaled-3, center_y -3, center_x + x_scaled +3, center_y +3 , fill=colour)   # точка (x)
        canv.create_text(center_x +x_scaled +10, center_y  -10, text = "x", fill = colour)

        canv.create_oval(center_x -3, center_y - y_scaled -3, center_x  +3, center_y - y_scaled +3 , fill=colour)   # точка (y)
        canv.create_text(center_x  +10, center_y - y_scaled -10, text = "y", fill = colour)

    # пунктир
    
        canv.create_line(center_x + x_scaled , center_y ,center_x + x_scaled , center_y - y_scaled  , fill="red", dash =2)
        canv.create_line( center_x , center_y - y_scaled ,center_x + x_scaled, center_y - y_scaled  , fill="red", dash =2)
    
def search_max_min(func, a : float , b : float , step :float = 0.01):
    '''
        функция ищет минимумы и максимумы функции на заданном отерзке a,b
        :param func: функция для которой ищутся максимумы и минимумы
        :param a:  начало отрезка
        :param b: конец отрезка
        :param step: шаг для перебора
        функция возвращает список в котором содержатся минимальные и максимальные зачения
    '''
    extremums=[]
    prev_value = func(a)
    current_value = func(a+step)
    next_value = func(a + 2*step)
    x = a+ step
    while x<= b - step:     # поиск минимума и максимума
        if current_value > prev_value and current_value > next_value:
            extremums.append((x,current_value,"max"))
        elif current_value < prev_value and current_value < next_value:
            extremums.append((x,current_value,"min"))
    
    # сдвиг значений
        prev_value = current_value
        current_value =next_value
        x += step
        next_value = func (x + step)

    return extremums

def multi_colored_gapsdef(func, a: int, b: int, scale, center_x, center_y , ):
    ''' 
        :param func: 
        :param  a: 
        :param b:
        :param scale: - масштаб
        :param center_x = координата центра координат по x
        :param center_y = координата центра координат по y
        
    '''
    length = b - a   # длина отрезка
    h = 0.001         # шаг для рисования графика функции
    n = int(length / h)
    for i in range(n-1):
        x0 =  (a+i*h)*scale
        y0 =  func(a+i*h)*scale 
        x1 = (a+(i+1)*h)*scale
        y1 =  func(a+(i+1)*h)*scale 
        if x0 < x1 and y0 < y1 :
            canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1 , fill="blue")
        else :
            canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1 , fill="red")

s = 50
canv = tk.Canvas(width = 1000, height = 800,bg='white')
canv.pack()
create_dpsk(center_x=400, center_y=400, scale=s)
draw_func(f, -4, 4, center_x=400, center_y=400, scale=s, colour="green") 
graph_func() 
designation_of_points(2, f, s, 400, 400,1, colour="red")  
#print(canv.__getitem__('bg'))
extremums=search_max_min(f,-4,4)
for x,y, type in extremums:
    if type =="max":
        designation_of_points(x,f,s,400,400,0,colour = "blue")
    elif type == "min":
        designation_of_points(x,f,s,400,400,0,colour="red")
multi_colored_gapsdef(f, -4, 4, center_x=400, center_y=400, scale=s)
    



tk.mainloop()