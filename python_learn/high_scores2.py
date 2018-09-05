#!/usr/bin/env python3

#High Scores 2.0
#演示嵌套序列

scores = []
choice = None

while choice != "0":
    print("""
High Scores 2.0

0 - Quit
1 - List Scores
2 - Add a Score
""")
    choice = input("Choice:")
    print()
    if choice == "0":
        print("Good-bye.")
    #显示最高分表
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score,name = entry
            print(name,"\t",score)
    #添加一条得分记录
    elif choice == "2":
        name = input("What is the player's name?:")
        score = int(input("What score did the player get?:"))
        entry = (score,name)
        scores.append(entry)
        scores.sort(reverse = True)
        scores = scores[:5]
    #处理无效选项
    else:
        print("Sorry,but",choice,"isn't a valid choice.")
