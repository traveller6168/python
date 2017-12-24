#!/user/bin/python3

import sys

def printinfo(str,*vartuple):
    print("定义的参数为：",str)
    print("循环取为定义的参数：")
    var_len = len(vartuple)
    print("元组个数为：",var_len)

    var = 0
    while var < var_len:
        print(vartuple[var])
        var += 1
    print("元组测试结束！")

    return;

printinfo(80,'test','hhh');

def changeme( mylist ):
    mylist.append([1,2,3,4]);
    print("函数内的值：",mylist)
    return
mylist = [10,20,30];
changeme(mylist);
print("函数外的指：",mylist)


def area(width,height):
    return width*height
def print_name(name):
    print("Welcome",name)
print_name("Runoob")
w = 4
h = 5
print("width =",w," heght =",h," area =",area(w,h))


def hello():
    print("Hello World!")

hello()



def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a,b = b,a+b
        counter += 1
f = fibonacci(10)
while True:
    try:
        print (next(f),end=" ")
    except StopIteration:
        sys.exit()


