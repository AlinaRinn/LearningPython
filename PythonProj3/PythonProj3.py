from random import random

# 1
# �������� �������, ������� ��������� ������ �� ������ ��� ���������� ���� � ���������� �� �� ������,
# �� � ������������� ����� ������� �� ���� ��� ����� ����.
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

# ������� ��������� N ������ ����� ���������. 

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(100)), end="\n\n")   

# ������� ���������, ��� ������ ���������� � ���������� ���������� ������� � ����� �����������.

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
# ��������� ��������-��������������� ������, ������� ��������� �� ����� Python, 
# ����������� ���������� ����������� ����� �� ������ ���� ������������� �������. ������ �� ����, ��� ����������� ����� ��������� �� �������

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
