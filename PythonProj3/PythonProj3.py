from random import random

# 1
# Напишите функцию, которая принимает строку из одного или нескольких слов и возвращает ту же строку,
# но с перевернутыми всеми словами из пяти или более букв.
# Hey fellow warriors -> Hey wollef sroirraw

def perevertish(a):
    b = a.split(' ')
    c = ''
    for i in b:
        if len(i) >= 5:
            c += ''.join(reversed(i))       
        c += ' '
    return c

print(perevertish(a = input("Vvedite stroku: ")), end="\n\n")

# Создать генератор N первых чисел Фибоначчи. 

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(100)), end="\n\n")   

# Создать декоратор, для вывода аргументов и результата выполнения функции с двумя переменными.

a = 10
b = 2

def cstmdecorator(deistvie):
    def wrap(a, b):
        print("--------------")
        print(float(deistvie(a, b)))
        print("--------------", end="\n\n")
    return wrap       

@cstmdecorator
def deistvie(a, b):
    c = random()
    return a * b / c

deistvie(1, 2)

# 2
# Используя объектно-ориентированный подход, создать программу на языке Python, 
# позволяющую определить температуру смеси по данным двух смешивающихся потоков. Исходя из того, что температуру можно вычислить по формуле

class Flow:
    def __init__(self, m, c, t):
        self.m = m
        self.c = c
        self.t = t

    def sum(self, other):
        return (self.m*self.t*self.c + other.m*other.c*other.t) / (self.m*self.c + other.m*other.c)

slv1 = Flow(10, 1000, 25)
slv2 = Flow(10, 1000, 15)

print(slv1.sum(slv2))
