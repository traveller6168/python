#!/usr/bin/env python3
people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That't too many buse.")
elif buses < cars:
    print("Maybe we could take the buse.")
else:
    print("We still can't decode.")

if people > buses:
    print("Alright, Let's just take the buses.")
else:
    print("Fine,let's stay home then.")