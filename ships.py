import random

board_player = [" "] * 9
board_pc = [" "] * 9

def show_board_player():
    print('Поле игрока')
    for i in range(0, 9, 3):
        print(board_player[i] + "|" + board_player[i + 1] + "|" + board_player[i + 2])
        if i < 6:
            print("-----")

def show_board_pc():
    print('Поле pc')
    for i in range(0, 9, 3):
        print(board_pc[i] + "|" + board_pc[i + 1] + "|" + board_pc[i + 2])
        if i < 6:
            print("-----")
def pc_ships():
    for i in range(3):
        empty = [i for i in range(9) if board_pc[i] == " "]
        board_pc[random.choice(empty)] = "*"

def  player_ships():
    while True:
        try:
            for i in range(1, 4):
                player_num = int(input(f"Ставь {i} корабль:  ")) - 1
                for j in range(3):
                    if board_player[player_num] == " ":
                        board_player[player_num] = "*"
                        show_board_player()
                        break
        except:
            print("Не правильный ввод")
            pass
        break


def player_shot():
    while True:
        try:
            player_num_shot = int(input('Введите куда стрелять (1-9): ')) - 1

            if player_num_shot < 0 or player_num_shot > 8:
                print("Введите число от 1 до 9")
                continue

            # Проверяем, стреляли ли уже сюда
            if board_pc[player_num_shot] == "X" or board_pc[player_num_shot] == "O":
                print("Сюда уже стреляли!")
                continue

            # Проверяем попадание
            if board_pc[player_num_shot] == "*":
                print("Попадание")
                board_pc[player_num_shot] = "X"  # X - попадание
                player_shot()

            else:
                print("Промах")
                board_pc[player_num_shot] = "O"  # O - промах
            show_board_pc()
            break

        except:
            print("Не правильный ввод")

def pc_shot():
    while True:
        pc_num_shot=random.randint(0,8)

        if board_player[pc_num_shot] == "X" or board_player[pc_num_shot] == "O":
            continue

        if board_player[pc_num_shot] == "*":
            print("ПК ПОПАЛ!!!")
            board_player[pc_num_shot] = "X"
            show_board_player()
            pc_shot()
            return
        else:
            print("Пк не попал...")
            board_player[pc_num_shot] = "O"
            break
    show_board_pc()

def chek_win_player():
        win_point=0
        for i in board_player:
            if i == "X":
                win_point +=1
                break
        if win_point == 3:
            print("Ты выйграл!Ура")
            show_board_pc()




def main():
    player_num=0
    print("Морской бой")
    # Ход игрока
    player_ships()
    # pc ход
    pc_ships()
    while True:
        #отладка pc
        print('+++++++++++++')
        show_board_pc()
        print('Стреляет игрок')
        player_shot()
        print('Стреляет пк')
        pc_shot()
main()