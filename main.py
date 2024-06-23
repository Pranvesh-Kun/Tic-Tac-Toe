from ascii import board, img
from computer import computer
from player import player

print(img)

rules = f"""How to play:\n
1) You can either play with computer or another player.\n
Rules: Players take turns putting their marks in empty squares. The first player to get 3 of their marks in a row(up, down, across, or diagonally) is the winner.\nWhen all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n\n2) In order to place a mark, enter the coordinate of the square.\n{board}\n(eg: a1, b3, c2)\n"""

game = True

while game:
    answer = input("Enter '1' to play with a computer, '2' to play with your friend, 'rules' to print the rules: ").lower()
    if answer == "rules":
        print(rules)
    elif answer == "1":
        computer()
        again = input("Do you want to play again? Y/N: ").lower()
        if again == "n":
            game = False
    elif answer == "2":
        player()
        again = input("Do you want to play again? Y/N: ").lower()
        if again == "n":
            game = False
    else:
        print("Enter a valid input.")
