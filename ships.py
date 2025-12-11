import random

board_player = [" "] * 9
board_pc = [" "] * 9

def show_board_player():
    print()
    for i in range(0, 9, 3):
        print(board_player[i] + "|" + board_player[i + 1] + "|" + board_player[i + 2])
        if i < 6:
            print("-----")

def show_board_pc():
    print()
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
    pass

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
        player_shot()
        pc_shot()
main()