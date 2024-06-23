import random


def computer():
    squares = {"a1": " ",
               "a2": " ",
               "a3": " ",
               "b1": " ",
               "b2": " ",
               "b3": " ",
               "c1": " ",
               "c2": " ",
               "c3": " "}
    list1 = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
    game = True
    while game:
        print(f"""
   a     b     c
      |     |     
1  {squares["a1"]}  |  {squares["b1"]}  |  {squares["c1"]}  
 _____|_____|_____
      |     |     
2  {squares["a2"]}  |  {squares["b2"]}  |  {squares["c2"]}  
 _____|_____|_____
      |     |     
3  {squares["a3"]}  |  {squares["b3"]}  |  {squares["c3"]}  
      |     |     """)
        while True:
            move = input("Enter the coordinate: ").lower()
            if move not in squares:
                print("Enter a valid coordinate: ")
            else:
                break
        list1.remove(move)
        squares[move] = "X"
        for i in ["a", "b", "c"]:
            if squares[f"{i}1"] == squares[f"{i}2"] == squares[f"{i}3"] == "X":
                print(f"""
                   a     b     c
                      |     |     
                1  {squares["a1"]}  |  {squares["b1"]}  |  {squares["c1"]}  
                 _____|_____|_____
                      |     |     
                2  {squares["a2"]}  |  {squares["b2"]}  |  {squares["c2"]}  
                 _____|_____|_____
                      |     |     
                3  {squares["a3"]}  |  {squares["b3"]}  |  {squares["c3"]}  
                      |     |     """)
                print("You WIN!")
                game = False
                break
        for i in ["1", "2", "3"]:
            if squares[f"a{i}"] == squares[f"b{i}"] == squares[f"c{i}"] == "X":
                print(f"""
                   a     b     c
                      |     |     
                1  {squares["a1"]}  |  {squares["b1"]}  |  {squares["c1"]}  
                 _____|_____|_____
                      |     |     
                2  {squares["a2"]}  |  {squares["b2"]}  |  {squares["c2"]}  
                 _____|_____|_____
                      |     |     
                3  {squares["a3"]}  |  {squares["b3"]}  |  {squares["c3"]}  
                      |     |     """)
                print("You WIN!")
                game = False
                break
        if squares["a1"] == squares["b2"] == squares["c3"] == "X":
            print(f"""
               a     b     c
                  |     |     
            1  {squares["a1"]}  |  {squares["b1"]}  |  {squares["c1"]}  
             _____|_____|_____
                  |     |     
            2  {squares["a2"]}  |  {squares["b2"]}  |  {squares["c2"]}  
             _____|_____|_____
                  |     |     
            3  {squares["a3"]}  |  {squares["b3"]}  |  {squares["c3"]}  
                  |     |     """)
            print("You WIN!")
            game = False
        elif squares["c1"] == squares["b2"] == squares["a3"] == "X":
            print(f"""
               a     b     c
                  |     |     
            1  {squares["a1"]}  |  {squares["b1"]}  |  {squares["c1"]}  
             _____|_____|_____
                  |     |     
            2  {squares["a2"]}  |  {squares["b2"]}  |  {squares["c2"]}  
             _____|_____|_____
                  |     |     
            3  {squares["a3"]}  |  {squares["b3"]}  |  {squares["c3"]}  
                  |     |     """)
            print("You WIN!")
            game = False
        if not game:
            break
        if len(list1) == 0:
            print("It is a tie.")
            break
        else:
            comp_move = random.choice(list1)
            squares[comp_move] = "O"
            list1.remove(comp_move)
            for i in ["a", "b", "c"]:
                if squares[f"{i}1"] == squares[f"{i}2"] == squares[f"{i}3"] == "O":
                    print("Computer WINS!")
                    game = False
                    break
            for i in ["1", "2", "3"]:
                if squares[f"a{i}"] == squares[f"b{i}"] == squares[f"c{i}"] == "O":
                    print("Computer WINS!")
                    game = False
                    break
            if squares["a1"] == squares["b2"] == squares["c3"] == "O":
                print("Computer WINS!")
                game = False
            elif squares["c1"] == squares["b2"] == squares["a3"] == "O":
                print("Computer WINS!")
                game = False
            if not game:
                break
