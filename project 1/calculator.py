#Create a calculator capable of performing addition, substraction, multiplication and divsion 
# operations on two numbers. Your program format the output in a readable manner.

num1 = int(input("Enteer first number: "))
num2 = int(input("Enter second number: "))

add = num1 + num2 
diff = num1 - num2
product = num1 * num2
div = num1 / num2


print ("the sum of ", num1, "and", num2, "is: ", add)
print ("the difference of ", num1, "and", num2, "is: ", diff)
print ("the product of ", num1, "and", num2, "is: ", product)
print ("the division of ", num1, "and", num2, "is: ", div)