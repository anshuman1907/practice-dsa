z= 5

def deco1(f):
    def inner(*a, **k):
        print("deco1")
        return f(*a, **k)
    return inner

def deco2(f):
    def inner(*a, **k):
        print("deco2")
        return f(*a, **k)
    return inner

@deco1
@deco2
def say():
    print("say")

say()


# class A:
#     lst = []

#     def __init__(self):
#         self.lst.append(len(self.lst))

# print(A().lst)
# print(A().lst)
# print(A().lst)




# class A:
#     def __enter__(self):
#         print("enter")
#         return self

#     def __exit__(self, *a):
#         print("exit")

# with A() as a:
#     print("inside")

# class A:
#     def __bool__(self):
#         return False

# if A():
#     print("yes")
# else:
#     print("no")


# def deco(f):
#     def wrapper(*a, **k): return f(*a, **k)
#     return wrapper

# @deco
# class A:
#     pass

# print(type(A))

# class D:
#     def __get__(self, obj, objtype):
#         return lambda: 99

# class A:
#     x = D()

# print(A().x())



# class A:
#     def __str__(self):
#         return "eval('1+2')"

# a = A()
# print(eval(str(a)))

# print("Top level")

# class A:
#     print("Inside A")
#     print("Inside A")


# print("After class A")

# class A:
#     def m1(self): print("A")

# class B(A):
   
#     def m(self): print("B")

# class C(A):
#     def m(self): print("C")

# class D(B, C): pass

# D().m()


# class A:
#     def __getattr__(self, name):
#         return name.upper()

# a = A()
# print(a.hello)



# class A:
#     funcs = []

#     for i in range(3):
#         def f(): return i
#         funcs.append(f)

# print([f() for f in A.funcs])


# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         print("Meta creating", name)
#         return super().__new__(cls, name, bases, dct)

# class A(metaclass=Meta):
#     def __init__(self):
#         print("Init A")

# a = A()

# class A:
#     def __new__(cls):
#         print("A.__new__")
#         return super().__new__(cls)

#     def __init__(self):
#         print("A.__init__")

# A()



# x = 1
# class A:
#     print(x)
#     x = 4
#     print(x)

# print(x)



# class A:
#     def __init__(self):
#         print("A", end=' ')

# class B(A):
#     def __init__(self):
#         print("B", end=' ')
#         super().__init__()

# class C(B, A):
#     pass

# C()


# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(B):
#     def show(self):
#         print("C")
#         super().show()

# C().show()


# class A:
#     def __init__(self):
#         self._x = 0

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, val):
#         self._x += val

# a = A()
# a.x = 5
# print(a.x)


# def func(): return "outside"

# class A:
#     func = func

#     def call(self):
#         return self.func()

# print(A().call())


# class A:
#     items = []

#     def __init__(self, val):
#         self.items.append(val)

# A(1)
# A(2)
# print(A.items)



# class A:
#     def greet(self):
#         print("A")

# class B(A):
#     def greet(lf):

#         print("B")

# class C(A):
#     pass

# class D(B, C):
#     pass

# D().greet()


# def append_to(val, lst=[]):
#     lst.append(val)
#     return lst

# print(append_to(1))
# print(append_to(2))


# funcs = []
# for i in range(3):
#     def f():
#         return i
#     funcs.append(f)

# print([f() for f in funcs])




# class A:
#     def method(self):
#         print("instance")

#     @staticmethod
#     def method():
#         print("static")

# A().method()




# class A:
#     x = 1

#     def __init__(self):
#         self.x = 2

# a = A()
# print(a.x)
# print(A.x)
