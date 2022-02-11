#Network Chuck Learn Python Episode 3

#playing with numbers - new change

name = "Stephen"

age = 47

actual_age = 47.65

print(name)
print(age)

print(type(name))
print(type(age))
print(type(actual_age))

#float is decimel and interger is a whole number
# exponents in math is **

#math = 5 ** 2 * 12 + 11 / 3 + 9 * 7
#print(5+7)
#print(math)

order = input()

price = 8

quantity = input("How many coffees would you like? \n")

total = price * int(quantity)

print("Thank you, your total is: $" + str(total) + " and we will have your " + str(quantity) + " coffees ready for you in a minute \n")