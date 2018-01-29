#!/usr/bin/env python3

#Hero's Inventory 3.0

inventory = ["sword","armor","shield","healing potion"]
print("Your items:")
for item in inventory:
    print(item)
#input("\nPress the enter key to continue.")

#获取列表得长度
print("You have",len(inventory),"items in you possession.")
#input("\nPress the enter key to continue.")

#利用in测试成员关系
if "healing potion" in inventory:
    print("You will live to fight another day.")

#显示切片
start = int(input("\nEnter the index number to begin a slice:"))
finish = int(input("Enter the index number to end the slice:"))
print("inventory[",start,":",finish,"] is",end=" ")
print(inventory[start:finish])
print("contunue!")



