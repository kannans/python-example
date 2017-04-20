# Calculate Triangle area

# Heros formula
# s = (a + b + c) / 2
# √(s(s-a)(s-b)(s-c))

a = 6
b = 3
c = 5

# Get input from user
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter thrid side: "))

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c))
print('The area of the triangle is %0.2f' % area)
