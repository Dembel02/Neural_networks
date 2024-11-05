# number = int(input('Введите число: '))
# factorial = 1

# while number > 1:
#     factorial = factorial * number
#     number = number - 1

# print(factorial)

number = int(input('Введите число: '))
# factorial = 1
for factorial in range(1, number):

    factorial = factorial * factorial
    # number = number - 1

print(factorial)


