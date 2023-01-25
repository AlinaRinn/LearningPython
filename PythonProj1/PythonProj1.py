import math

# 1
a = [-3, -19, 4, -15, 2, -10, -3, 1, -11, 19]
print(a)

# 2
for i in range(0,10,3):
    print(a[i])
# or
print(a[::3])

# 3
print(a[6:0:-1])

# 4
list.reverse(a)
print(a)

# 5
list.sort(a)
print(a)

# 6
print("\nax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c
print("D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("No roots")

# 7
# Yes, I choose very lazy decision =) 
a = [2, 3, 5, 7, 11]
for i in range(2, 201, 1):
    if i % 2 != 0:
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0: 
            list.append(a, i)
print(a)

# 8
a = ["A", "E", "I", "O", "U", "Y"]

while(True):
    c = input("Enter string: ")
    c = c.upper()
    glasnie = 0
    if c.isalpha():
        for i in range(0, len(a), 1):
             glasnie += c.count(a[i])
        vsego = len(c)
        print("glasnie: ", glasnie, " ", glasnie/vsego*100, "%")
        print("soglasnie: ", vsego-glasnie, " ",100-(glasnie/vsego*100), "%")
    else:
        print("Enter only letters")
    
