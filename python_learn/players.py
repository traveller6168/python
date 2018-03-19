#!/usr/bin/env python3

class Player:
    def __init__(self,name):
        self._name = name
        self._score = 0
    def reset_score(self):
        self._score = 0
    def incr_score(self):
        self._score = self._score +1

    def get_name(self):
        return self._name
    def __str__(self):
        return "name = '%s',score = %s" %(self._name,self._score)
    def __repr__(self):
        return 'Player(%s)' % str(self)

class Human(Player):
    def __repr__(self):
        return ('Human(%s)' % str(self))
    def get_move(self):
        while True:
            try:
                n = int(input('%s move (1 - 10):' % self.get_name()))
                if 1 <= n <= 10:
                    return n
                else:
                    print('0ops!')
            except:
                print('Oops!')


import random
class Computer(Player):
    def __repr__(self):
        return 'Computer(%s)' % str(self)
    def get_move(self):
        return random.randint(1,10)

def play_undercut(p1,p2):
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    print("%s move: %s" % (p1.get_name(),m1))
    print("%s move: %s" % (p2.get_name(),m2))
    if m1 == m2 - 1:
        p1.incr_score()
        print('!')
        return p1,p2,'%s wins!' % p1.get_name()
    elif m2 ==  m1 - 1:
        p2.incr_score()
        print('@')
        return p1,p2,'%s wins!' % p2.get_name()
    else:
        return p1, p2, 'draw: no winner!'
        print('#')


c = Computer('Hal Bot')
h = Human('Lia')
r = Human('LOU')
print(play_undercut(c,h))
print(play_undercut(r,h))