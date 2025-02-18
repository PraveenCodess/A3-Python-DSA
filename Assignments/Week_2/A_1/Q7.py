# Write a function named celsius_to_fahrenheit that converts Celsius to
# Fahrenheit and prints the result. (Formula: (Celsius * 9/5) + 32 = Fahrenheit)


def celsius_to_fahrenheit(n):
    f = (n * 9 / 5) + 32
    print(f)


n = int(input())
celsius_to_fahrenheit(n)
