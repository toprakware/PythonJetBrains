state_matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
winner = []
isXsTurn = True


def print_field(matrix):
    print("-" * 9)
    for i in range(3):
        print("| " + " ".join(matrix[i]) + " |")
    print("-" * 9)


def check_winner(matrix):
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != ' ':
            winner.append(state_matrix[i][0])

        elif matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != ' ':
            winner.append(state_matrix[0][i])

    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != ' ' or \
       matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != ' ':
        winner.append(state_matrix[1][1])


print_field(state_matrix)

while True:
    if isXsTurn:
        played_cell = [int(coord) for coord in input("Enter your move to play as X: ").split()]
        try:
            if played_cell[0] not in [1, 2, 3] or played_cell[1] not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
                continue
            elif state_matrix[played_cell[0] - 1][played_cell[1] - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                isXsTurn = False
                state_matrix[played_cell[0] - 1][played_cell[1] - 1] = "X"
        except ValueError:
            print("You should enter numbers!")
            
    else:
        played_cell = [int(coord) for coord in input("Enter your move to play as O: ").split()]

        try:
            if played_cell[0] not in [1, 2, 3] or played_cell[1] not in [1, 2, 3]:
                print("Coordinates should be from 1 to 3!")
                continue
            elif state_matrix[played_cell[0] - 1][played_cell[1] - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                isXsTurn = True
                state_matrix[played_cell[0] - 1][played_cell[1] - 1] = "O"
        except ValueError:
            print("You should enter numbers!")
            
    print_field(state_matrix)
    check_winner(state_matrix)

    if len(winner) == 1:
        print(f"{winner[0]} wins")
        break
    
    if all([state_matrix[i][j] != " " for i in range(3) for j in range(3)]):
        print("Draw")
        break
