#1
s='345'
str(s)
sc=[int(a)for a in s]
sc=sum(sc)
#print(sc)

x=69696969
s=0
while x>0:
        d=x%10
        s=s+d
        x=x//10
#print(s)

#2
def reverse_number(n):
    # Данная функция Преобразует число в строку, затем переворачиваем строку и возвращаем в виде числа
    return int(str(n)[::-1])
number = int(input("Введите натуральное число: "))  
reversed_number = reverse_number(number)  
#print("Число в обратном порядке:", reversed_number)

#3
def p(x):
        d=2
        while d*d<=x:
                if x%d==0:
                        return 0
                d+=1
        return 1
x=100
print(p(x))


