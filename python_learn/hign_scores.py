#!/usr/bin/env python3

#High Scores
#演示列表方法

scores = []
choice = None

while choice != "0":
    print("""
            High Scores
            
            0  - Exit
            1  - SHow Scores
            2  - Add a Score
            3  - Remove a Score
            4  - Sort Scores
            """)
    choice = input("Choice:")
    print()
    if choice == "0":
        print()
        input("\n\nPress the enter key to exit.")
    elif choice == '1':
        print("High Scores")
        for score in scores:
            print(score)
    elif choice == '2':
        score = int(input("What score did you get?:"))
        scores.append(score)
    elif choice == '3':
        score = int(input("Remove whice score?:"))
        if score in scores:
           scores.remove(score)
        else:
            print(score,"isn't in the high scores list.")
    elif choice == '4':
        scores.sort(reverse=True)
    else:
        print("Sorry,but",choice,"isn't a valid choice.")
