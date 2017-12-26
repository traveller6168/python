class MYClass:
  i = 12345
  def f(self):
      return 'hello world'

x = MYClass()


print("MyClass 类的属性 i 为 ：", x.i)
print("Myclass 类的方法 f 输出为 ： ", x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, 4.5)
print(x.r, x.i)

class people:
    name = ''
    age = 0

    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
         print("%s 说：我 %d 岁" %(self.name,self.age))

p = people('runoob',10,30)
p.speak()

class student(people):
    grade =  ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

s = student('ken',10,60,3)
s.speak()


class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法