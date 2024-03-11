#for loop

for i in range(11):
    print(i * 5)

for i in range(1, 11):
    print(i * 2)

num = 1
for i in range(5,11):
    num = num + 1
    print(i * num)


import math
def fact(n):
    return(math.factorial(n))
num1 = int(input("Enter the number:"))
f = fact(num1)
print("Factorial of", num1, "is", f)

num2 = int(input("enter your number: "))

if (num2 % 2) == 0: 
    print(num2 / 2)

else:
    print(num2 * 3 + 1)

#while loop
    
number = 10
while number > 0:
    print(number)
    number -= 1

name = input("enter your name: ")
if name != quit:
    input("please, enter your name again: ")

else: 
    print("thanks")


number1 = 10
while  number1 < 20:
    print(number1)
    number1 += 2

number2 = int(input("enter your number: "))

if number2 == 7:
    print("you guessed the number")

else:
    input("enter number again: ")

number3 = 1
while number3 < 11:
    print(number3 * number3)
    number3 += 1



    






