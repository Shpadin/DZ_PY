task = int(input('введие номер задачи от 1 до 5: '))
match task:
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет
    case 1:
        den_nedeli = int(input('введите цифру, обозначающую день недели от 1 до 7:  '))

        if den_nedeli == 6 or den_nedeli == 7 :
            print(den_nedeli,' -> ДА')
        # elif den_nedeli == 7:
        #     print('ДА')
        else:
            print(den_nedeli, ' -> Нет')
# ------------

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    case 2:
        for x in [True,False]:
            for y in [True,False]:
                for z in [True,False]:
                    print(f'x = {x} y = {y} z = {z}', end ='->' )
                    print(not (x and y and z) == (not x) or (not y) or (not z))
            
# ----------------------

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
    case 3:
        abscissa_X = int(input('введите координату X: '))
        ordinate_Y = int(input('введите координату y: '))

        if abscissa_X == 0 or ordinate_Y == 0:
            print('введите координаты X ≠ 0 и Y ≠ 0')
        elif abscissa_X>0 and ordinate_Y>0:
            print('-> 1')
        elif abscissa_X>0 and ordinate_Y<0:
            print('-> 4')
        elif abscissa_X<0 and ordinate_Y>0:
            print('-> 2')
        else:
            print('-> 3')

# --------------------

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

    case 4:
        quarter = int(input('Введите номер четверти (1, 2, 3, 4): '))
        match quarter:
            case 1:
                 print('x>0,y>0')
            case 2:
                 print('x<0,y>0')
            case 3:
                 print('x<0,y<0')
            case 4:
                print('x>0,y<0')
            case _:
                print('Введено не число четверти')


# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
    case 5:
        abscissa_X1 = int(input('введите координату X1: '))
        ordinate_Y1 = int(input('введите координату Y1: '))
        abscissa_X2 = int(input('введите координату X2: '))
        ordinate_Y2 = int(input('введите координату Y2: '))

        distance= ((abscissa_X1-abscissa_X2)**2+(ordinate_Y1-ordinate_Y2)**2)**0.5
        print (distance)
    case _:
        print('Это нам не задавали')