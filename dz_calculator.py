import tkinter as tk
from tkinter import font
Evalute = 0

def press_butt (n):
    """
    Функция для нажатия кнопок 
    """
    global Evalute
    if Evalute == 0 :
        text = str(display["text"])
        text += f"{n}"
        display["text"]= text
    else:
        display["text"] = f"{n}"
    Evalute = 0



def calculation():
    """
    функция для вычисления результата вычислений
    """
    global Evalute
    text = str(display["text"])
    if text[-1] in '+-*/':
        text = text[:-1] + text[-1]+text[:-1]
    display["text"]= eval(text)
    Evalute = 1
        
def delit():
    """
    Функция для удаение с помощью среза последнего элемента
    """

    text = str(display["text"])
   
    display["text"]= text[:-1]

def clear():
    display["text"]=f""



#создаем окно
window = tk.Tk()
window.title("Калькулятор")
window.geometry('480x617')
window.resizable(False,False)

#создаем окно для вывода иформации
frame = tk.Frame( master=window, relief= tk.SUNKEN , borderwidth = 7)
frame.grid(row=0,column=0,columnspan=5)
display=tk.Label(master = frame ,width=65,height=4,text="")
display.grid(row=0,column = 0,columnspan=10)


#Размер  текста на кнопке
button_font = font.Font(size =10)
#кнопки
btn_7 =tk.Button(window ,width=10,height=8, text="7",command=lambda:press_butt(7), font = button_font)
btn_7.grid(row=1 ,column =0,sticky="w")

btn_8 =tk.Button(master = window ,width=10,height=8, text="8",command=lambda:press_butt(8), font = button_font)
btn_8.grid(row=1 ,column =1,sticky="w")

btn_9 =tk.Button(master = window ,width=10,height=8, text="9",command=lambda:press_butt(9), font = button_font)
btn_9.grid(row=1 ,column =2,sticky="w")
#деление
btn_div =tk.Button(master = window ,width=10,height=8, text="÷",command=lambda:press_butt("/"), font = button_font)
btn_div.grid(row=1 ,column =3,sticky="w")

btn_4 =tk.Button(master = window ,width=10,height=8, text="4",command=lambda:press_butt(4), font = button_font)
btn_4.grid(row=2 ,column =0,sticky="w")

btn_5 =tk.Button(master = window ,width=10,height=8, text="5",command=lambda:press_butt(5), font = button_font)
btn_5.grid(row=2 ,column =1,sticky="w")

btn_6 =tk.Button(master = window ,width=10,height=8, text="6",command=lambda:press_butt(6), font = button_font)
btn_6.grid(row=2 ,column =2,sticky="w")
#умножение
btn_mul =tk.Button(master = window ,width=10,height=8, text="×",command=lambda:press_butt("*"), font = button_font)
btn_mul.grid(row=2 ,column =3,sticky="w")

btn_1 =tk.Button(master = window ,width=10,height=8, text="1",command=lambda:press_butt(1), font = button_font)
btn_1.grid(row=3 ,column =0,sticky="w")

btn_2 =tk.Button(master = window ,width=10,height=8, text="2",command=lambda:press_butt(2), font = button_font)
btn_2.grid(row=3 ,column =1,sticky="w")

btn_3 =tk.Button(master = window ,width=10,height=8, text="3",command=lambda:press_butt(3), font = button_font)
btn_3.grid(row=3 ,column =2,sticky="w")
#вычитание
btn_sub =tk.Button(master = window ,width=10,height=8, text="-",command=lambda:press_butt("-"), font = button_font)
btn_sub.grid(row=3 ,column =3,sticky="w")
#удаление последнего элемента в стороке
btn_del =tk.Button(master = window ,width=10,height=7, text="⌫",command=delit, font = button_font)
btn_del.grid(row=4 ,column =0,sticky="w")

btn_0 =tk.Button(master = window ,width=10,height=7, text="0",command=lambda:press_butt(0), font = button_font)
btn_0.grid(row=4 ,column =1,sticky="w")

btn_fraction =tk.Button(master = window ,width=10,height=7, text=".",command=lambda:press_butt("."), font = button_font)
btn_fraction.grid(row=4 ,column =2,sticky="w")
#сумма
btn_sum =tk.Button(master = window ,width=10,height=7, text="+",command=lambda:press_butt("+"), font = button_font)
btn_sum.grid(row=4 ,column =3,sticky="w")
#полное стирание
btn_fraction =tk.Button(master = window ,width=13,height=8, text="С",command = clear , font = button_font)
btn_fraction.grid(row=1 ,column =4,sticky="w")
#результат
btn_fraction =tk.Button(master = window ,width=13,height=25, text="=",command = calculation , font = button_font)
btn_fraction.grid(row=2 ,column =4,rowspan=4,sticky="w")

window.mainloop()