# File : CS112_A1_T2_Game2_20230315
# Purpose :Number scrabble is played with the list of numbers between 1 and 9. Each player takes
# turns picking a number from the list. Once a number has been picked, it cannot be picked
# again. If a player has picked three numbers that add up to 15, that player wins the game.
# However, if all the numbers are used and no player gets exactly 15, the game is a draw.

# Author : Mohamed Ahmed Kotb
# ID : 20230315


# List of available numbers
num_pick = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Welcome message and getting player names
print("Welcome to number Scrabble game..")
print("The First one who picks three numbers up to 15 will win.")
ply1 = input("Please Enter the name of first player: ")
ply2 = input("Please Enter the name of second player: ")

# Initialize variables for sums, current player, and turns
ply1_sum = 0
ply2_sum = 0
current = 1
turns = 0

# Main game loop
while True:
    # Check if there are no numbers left, declare if the game draw
    if not num_pick:
        print("Game is draw...")
        break

    # Player 1 turn
    if current == 1:
        print(ply1, ":")
        print("The available numbers are:", num_pick)

        # Player 1 chooses a number
        num = int(input("Choose the number that you want: "))

        # Checking if the input is not valid
        if num not in num_pick:
            print("Error!!! you entered a wrong number.")
            continue

        # Update Player 1 sum and check for win condition
        ply1_sum += num
        if ply1_sum == 15 and turns >= 2:
            print("The sum of ", ply1, "=", ply1_sum)
            print(ply1, "is the winner...")
            break

        # Remove chosen number from available numbers and switch to Player 2 turn
        num_pick.remove(num)
        print("The sum of ", ply1, "=", ply1_sum)
        current = 2

    # Check if there are no numbers left, declare if the game draw
    if not num_pick:
        print("Game is draw...")
        break

    # Player 2 turn
    if current == 2:
        print(ply2, ":")
        print("The available numbers are:", num_pick)

        # Player 2 chooses a number
        num = int(input("Choose the number that you want: "))

        # Checking if the input is not valid
        if num not in num_pick:
            print("Error!!! you entered a wrong number.")
            continue

        # Update Player 2 sum and check for win condition
        ply2_sum += num
        if ply2_sum == 15 and turns >= 2:
            print("The sum of ", ply2, "=", ply2_sum)
            print(ply2, "is the winner...")
            break

        # Remove chosen number from available numbers and switch to Player 1 turn
        num_pick.remove(num)
        print("The sum of ", ply2, "=", ply2_sum)
        current = 1

    # Increase game turns to ensure to pick three numbers or more
    turns += 1
