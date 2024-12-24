field = [[" "] * 3 for i in range(3)]

def square():
    print("------------")
    print("  0 | 1 | 2")
    for i in range(3):
        row = " | ".join(field[i])
        print("------------")
        print(f"{i} {row}")
    print("------------")

def user_input():
    while True:
        cords = list(map(int, input("Введите координаты (от 0 до 2):").split()))
        x, y = cords
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Ошибка ввода. Введите корректные данные!")
            continue
        
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        
        return x, y

def win():
    win_combination = [
        ((0, 0), (0, 1), (0, 2)), 
        ((1, 0), (1, 1), (1, 2)), 
        ((2, 0), (2, 1), (2, 2)), 
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)), 
        ((0, 2), (1, 2), (2, 2)), 
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    ]
    
    for cord in win_combination:
        combination = [field[c[0]][c[1]] for c in cord]
        if combination == ["X", "X", "X"]:
            print("Победа за X!")
            return True
        
        if combination == ["0", "0", "0"]:
            print("Победа за 0!")
            return True
        
    return False
                
def app():
    count = 0
    while True:
        square()
        count += 1
        
        if count % 2 == 1:
            print("Ходит крестик!")
            x, y = user_input()
            field[x][y] = "X"
        else:
            print("Ходит нолик!")
            x, y = user_input()
            field[x][y] = "0"
        
        if win():
            square()  
            break
        
        if count == 9:
            print("Игра окончена. Ничья!")
            square()  
            break

app()

        
    