# Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.
# Example 1
# Enter bill amount = 80000
# You got 30% discount
# Your final bill is Rs. 56000


def discount(n):
    if n >= 50000:
        print("30% Discount")
        dis = (30 / 100) * n
        print(n - dis)
    elif n >= 40000:
        print("25% Discount")
        dis = (25 / 100) * n
        print(n - dis)
    elif n >= 30000:
        print("20% Discount")
        dis = (20 / 100) * n
        print(n - dis)
    elif n >= 10000:
        print("10% Discount")
        dis = (10 / 100) * n
        print(n - dis)
    else:
        print("No Discount")


discount(80000)
