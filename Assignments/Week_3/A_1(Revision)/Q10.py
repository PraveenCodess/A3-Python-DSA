# Create a function that takes the number of daily average recovered
# cases recovers, daily average new_cases, current active_cases, and returns
# the number of days it will take to reach zero cases.
# end_corona(4000, 2000, 77000) ➞ 39
# end_corona(3000, 2000, 50699) ➞ 51
# end_corona(30000, 25000, 390205) ➞ 79
# The number of people who recover per day recovers will always be greater
# than daily new_cases.
# Be conservative and round up the number of days needed


def corona(rec, new, act):
    d = rec - new
    print((act // d) + 1)


rec, new, act = map(int, input().split(","))
corona(rec, new, act)


# def end_corona(recovers, new_cases, active_cases):
#     count = 0
#     while active_cases > 0:
#         active_cases -= recovers
#         active_cases += new_cases
#         count += 1
#     return count
