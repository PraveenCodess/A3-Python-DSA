# Take Salary as input from User and Update the salary of an employee.
# salary less than 10,000, 5 % increment
# salary between 10,000 and 20, 000, 10 % increment
# salary between 20,000 and 50,000, 15 % increment
# salary more than 50,000, 20 % increment


def salary(n):
    if n < 10000:
        inc = (5 / 100) * n
        print(n + inc)
    elif n <= 20000:
        inc = (10 / 100) * n
        print(n + inc)
    elif n <= 50000:
        inc = (15 / 100) * n
        print(n + inc)
    else:
        inc = (20 / 100) * n
        print(n + inc)


salary(50000)
