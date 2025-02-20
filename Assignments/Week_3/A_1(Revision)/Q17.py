# A financial institution provides professional services to banks and
# claims charges from the customers based on the number of man-days
# provided. Internally, it has set a scheme to motivate and reward staff to
# meet and exceed targeted billable utilization and revenues by paying a
# bonus for each day claimed from customers in excess of a threshold
# target.
# This quarterly scheme is calculated with a threshold target of 32 days per
# quarter, and the incentive payment for each billable day in excess of such
# threshold target is shown as follows:


# Please note that incentive payment is calculated progressively. As an
# example, if an employee reached total billable days of 45 in a quarter,
# his/her incentive payment is computed as follows:
# 32*0 + 8*325 + 5*550 = 5350
# Write a function to read the billable days of an employee and return the
# bonus he/she has obtained in that quarter.
# Examples:
# bonus(15) ➞ 0
# bonus(37) ➞ 1625
# bonus(50) ➞ 8200


def bonus(n):
    if n <= 32:
        return 0
    elif n >= 33 and n <= 40:
        t1 = n - 32
        return 32 * 0 + t1 * 325
    elif n >= 41 and n <= 48:
        t1 = n - 32
        t2 = t1 - 8
        return 32 * 0 + 8 * 325 + t2 * 550
    else:
        t1 = n - 32
        t2 = t1 - 8
        t3 = t2 - 8
        return 32 * 0 + 8 * 325 + 8 * 550 + t3 * 600


n = int(input())
print(bonus(n))


# def bonus(days):
#     total = 0
#     for i in range(1, days + 1):
#         if 32 < i <= 40:
#             total += 325
#         if 40 < i <= 48:
#             total += 550
#         if i > 48:
#             total += 600
#     return total
