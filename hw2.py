                #Задача 1
#1) Создайте плейлист из 10 любимых песен, поменяйте 4-й с 8-м и выведите на экран весь плейлист:

def p1():

    mus = ["Кино", "Номера", "Fly", "Asqua", "Люби меня", "Самурай", "Родная пой", "In LOve", "Fire man", "Colors"]
    print(mus)
    mus[4], mus[8] = mus[8],mus[4]
    print(mus)

# p1()

            # Задача 2.1
# 2 Создайте список из 15 элементов. Сделайте срез от 2-го индекса до 7-го:

def p2():

    lest = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P"]
            # 0   1    2    3    4    5    6    7    8    9    10   11   12   13   14  15  
    print(lest)
    print(lest[2:8])

# p2()


            # Задача 2.2

def p3():

    num = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16]
        #  0 1 2 3 4 5 6 7 8  9  10 11 12 13 14 15
    print(num)
    print(num[2:8])

# p3()

                    # Задача 3
# 3 Создайте список чисел и выведите их в обратном порядке:

def p4():

    num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    print(num)
    print(num[::-1])

# p4()


                   # Задача 4
# 4 Даны два списка, удалите все элементы первого списка из второго:
 # # a = [1, 3, 4, 5] 
# # b = [4, 5, 6, 7]

def p5():

    a = [1, 3, 4, 5] 
    b = [4, 5, 6, 7]
    c =a +b
    print(c)
    print(list(set(c)))

# p5()


                    # Задача 5
# Найдите наименьший элемент в списке из задания 2:

def p6():

    num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    print(min(num))

# p6()

            # Задача 6
# Удалите все элементы из списка, созданного в задании 2:

def p7():

    num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    del num[0:17]
    print(num)

# p7()

            # Задача 7
# Найдите сумму элементов в списке из задания 2:

def p8():

    num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    print(sum(num))

# p8()

            # Задача 8
# Найдите среднее арифметическое  элементов  списке из задания 2:

def p9():

    num =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    print(sum(num)/ 16)

# p9()

            # Задача 8
# Есть список numbers. Выясните сколько раз цифра 110 встречается в списке

def p10():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
    216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110]
    print(numbers.count(110))

# p10()











































































































































