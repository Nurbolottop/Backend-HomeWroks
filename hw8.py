# Создать калькулятор на функцииф с именем calc  и параметрами (a, b, operation) . Описание входных параметров:
# Первое число(дробное число) вы сами даете в аргументах
# Второе число(дробное число) вы сами даете в аргументах
# Действие над ними: 
    # 1) + Сложить
    # 2) - Вычесть
    # 3) * Умножить
    # 4) / Разделить
# Сделайте момент где если пользователь делит число на 0, нужно вывести “На ноль делить нельзя”
# В остальных случаях функция должна возвращать "Операция не поддержи


    #Пример 1
def cal():
    while True:
        a=int(input("Введите первое число: "))
        b=int(input("Введите второе число: "))
        c=input("Выберите что хотите сделать... 1) + Сложить; 2) - Вычесть; 3) * Умножить; 4) / Разделить)")
        if c == "1":
            print("Ваш ответ:",a+b)
        elif c == "2":
            print("Ваш ответ:",a-b)
        elif c == "3":
            print("Ваш ответ:",a*b)
        elif a==0 or b==0 and c=="/":
            print("На ноль делить нельзя")
        elif c =="4":
            print("Ваш ответ:",a/b)
        else:
            nurbolot= print
            nurbolot("Операция не поддерживается")

# cal()







        #ПРИМЕР 2
def calc(n1, n2, op):
    if op =="1":
        print(n1+n2)
    elif op == "2":
        print(n1-n2)
    elif op =="3":
        print(n1*n2)
    elif op =="4":
        try:
            print(n1/n2)
        except:
            print("На ноль делить нельзя")
    else:
        print("EROR>>>")
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=input("Выберите что хотите сделать... 1) + Сложить; 2) - Вычесть; 3) * Умножить; 4) / Разделить)")

calc(a,b,c)























