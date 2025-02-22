#LISTS EXAMPLES

#l=['a','b','c']
#print(l)
#for i in l:
#    print(i)
    #print(l)
#print(l[0])
#print(l[1])
#print(l[2])
#l.append("d")
#print(l[3])
#l.extend(["e","f"])
#print(l)
#for i in l:
#    print(i)
#l.remove("e")
#print(l)
#l.pop(2)
#print(l)
#l.sort()
#print(l)
#l.reverse()
#print(l)
#a=l.index("a")
#print(a)

#TUPLE EXAMPLES
#t=(10,20,20,30)
#print(t)
#print(t[0])
#print(t[1])
#print(t[2])
#for i in t:
#    print(i)
#print(len(t))
#print(t.count(20))

#TUPLE TO LIST CONVERSIONS

#l=(1,2,3)
#print(l)
#print(list(l))
#print(tuple(l))

#DICTIONARIES
#dict_name={name:'key',..............}
#d={"a":1,"b":2,"c":3}
#print(d)
#print(d["a"])
#d["d"]=4
#print(d["d"])
#d["a"]=5
#print(d["a"])
#d.pop("b")
#print(d["a"])
#print(d.popitem())
##to get the keys
#print(d.keys())
##to get the values
#print(d.values())
##to get the items
#print(d.items())

#SETS
#s={1,2,3,3,False}
#print(s)

#ARMSTRONG NUMBER
'''a=int(input("Enter a number:"))
temp=a
sum=0
while temp>0:
    remainder=temp%10
    sum=sum+(remainder*remainder*remainder)
    temp=temp//10
if a==sum:
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")
'''
#CLASS EXAMPLE
'''class bird:
        def __init__(self):
            self.color=None
            self.height=None
        #values from user
        def setvalue(self,color,height):
                #a=input(print("enter the color of the bird:"))
                #b=input(print("enter the height of the bird in inches:"))
                self.color=color
                self.height=height
        #display them
        def getvalue(self):
                print("color of the bird:",self.color)
                print("height of the bird:",self.height)
a=bird()
a.setvalue("red",0.1)
a.getvalue()
'''
#CLASS ANOTHER EXAMPLE
'''class bird:
    def fly(self):
        print("Flying")
    def swim(self):
        print("Swimming")
callbird=bird()
callbird.fly()
callbird.swim()
callbird.fly=10
callbird.flyy=20
callbird.flyyy=30
callbird.flyyyy="app"
print(callbird.fly)
print(callbird.flyy)
print(callbird.flyyy)
print(callbird.flyyyy)
calling=bird()
calling.swim="snake"
calling.swimm=523
calling.swimmm="l"
calling.swimmmm="4"
print(calling.swim)
print(calling.swimm)
print(calling.swimmm)
print(calling.swimmmm)
'''
'''(EXAMPLE ANOTHER)class bird:
        #values from user
        def setvalue(self,color,height):
                #a=input(print("enter the color of the bird:"))
                #b=input(print("enter the height of the bird in inches:"))
                self.color=color
                self.height=height
        #display them
        def getvalue(self):
                print("color of the bird:",self.color)
                print("height of the bird:",self.height)
a=bird()
a.setvalue("red",0.1)
a.getvalue()
'''

#INHERITANCE

#SINGLE INHERITANCE
'''class A:
        def a():
            print("a class")
class B(A):
        def b():
            print("b class")
B.a()
B.b()
'''

#MULTIPLE INHERITANCE
'''class A:
    def a():
        print("a class")
class B:
    def b():
        print("b class")
class C(A,B):
    def c():
        print("c class")
C.a()
C.b()
C.c()
'''

'''
#MULTILEVEL INHERITANCE
class A:
    def a():
        print("a class")
class B(A):
    def b():
        print("b class")
class C(B):
    def c():
        print("c class")
C.a()
C.b()
C.c()
'''
#HYBRID INHERITANCE
'''class A:
    def a():
        print("a class")
class B(A):
    def b():
        print("b class")
class C:
    def c():
        print("c class")
class D(B,C):
    def d():
        print("d class")
D.a()
D.b()
D.c()
D.d()
'''    

'''
#SINGLE INHERITANCE
class A:
    def a(self):
        print("a class")
class B(A):
    def b(self):
        print("b class")
obj=B()
obj.a()
obj.b()
'''

'''
#MULTIPLE INHERITANCE
class A:
    def a(self):
        print("a class")
class B():
    def b(self):
        print("b class")
class C(A,B):
    def c(self):
        print("c class")
obj=C()
obj.a()
obj.b()
obj.c()
'''

'''
#MULTILEVEL INHERITANCE
class A:
    def a(self):
        print("a class")
class B(A):
    def b(self):
        print("b class")
class C(B):
    def c(self):
        print("c class")
obj=C()
obj.a()
obj.b()
obj.c()
'''

'''
#HIERARCHICAL INHERITANCE
class A:
    def a(self):
        print("a class")
class B(A):
    def b(self):
        print("b class")
class C(A):
    def c(self):
        print("c class")
obj=C()
obj.a()
obj.c()
obj=B()
obj.b()
obj.c()
'''

'''
#HYBRID INHERITANCE
class A:
    def a(self):
        print("a class")
class B(A):
    def b(self):
        print("b class")
class C(A):
    def c(self):
        print("c class")
class D(C,B,A):
    def d(self):
        print("d class")
obj=D()
obj.a()
obj.c()
obj.d()
obj.b()
'''

#REGULAR EXPRESSIONS
'''
#findall
import re
a="the rain in espana"
b=re.findall("in",a)
print(b)
'''

'''
#search
import re
a="the rain is espana"
b=re.search("the.*spain$",a)
if a:
    print("ok")
else:
    print("not ok")
'''

'''
#split
import re
a="the rain in espana"
b=re.split("\s",a)
print(b)
'''

'''
#sub
import re
a = "the rain in espana"
b = re.sub("\s", "*", a)
print(b)
'''
