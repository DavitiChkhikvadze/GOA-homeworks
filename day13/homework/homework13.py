for i in range(1, 50):
    if i // 3 % 0:
        print("fizz")
    elif i // 5 % 0:
        print("buzz")
    elif i // 5 % 0 and i // 3 % 0:
        print("fizzbuzz")
    else:
        print(i)


user_number = int(input("enter your number here: "))

if user_number > 0:
    print("your chosen number is positive")
elif user_number < 0:
    print("your number is negative")
else:
    print("your number is zero")


for i in range(1, 100, 2):
    print(i)





