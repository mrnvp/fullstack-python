square = [[' ', ' ', ' '] for i in range(3)]

def show():
    print(f"    0 | 1 | 2")
    print("--------------")
    for i in range(3):
        print(f"{i} | {square[i][0]} | {square[i][1]} | {square[i][2]} ")
        print('--------------')

def input_users():
    while True:
        cords = input("          Введите ваш ход:").split()
        if len(list(cords)) < 2:
            print("Ошибка! Введите 2 координаты")
            continue
        
        x, y = map(int, cords)
        
        if 0 <= x <= 2 or 0 <= y <= 2:
            if square[x][y] == " ":
                return x, y
            else:
                print("Клетка заполнена")
                continue
        else:
            print("Ошибка! Выход за область координат")
            continue

def check_win():
    win_combination = (((0, 0), (0, 1), (0, 2)),((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)),((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    
    for comb in win_combination:
        combin = []
        
        for c in comb:
            combin.append(square[c[0]][c[1]])
            
        if combin == ['X','X','X']:
            print("Выиграл крестик!")
            return True
        
        if combin == ['0','0','0']:
            print("Выиграл нолик!")
            return True
        
    return False

num = 0

while True:
    show()
    num +=1
    
    if num % 2 == 1:
        print("Ходит крестик")
    else: 
        print("Ходит нолик")
    
    x, y = input_users()
    
    if num % 2 == 1:
        square [x][y] = 'X'
    else: 
       square [x][y] = '0'
    
    if check_win():
        break
    
    if num == 9:
        print('Победила дружба')
        break
