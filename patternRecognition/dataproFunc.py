# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y,z):
   result = (x * y)-(y*z)
   
   return result

num1 = 9
num2 = 8
num3=5

print("The sum is", add_numbers(num1, num2,num3))