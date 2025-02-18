# Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)


t = int(input())
w = int(input())
l = int(input())
tie = t - (w + l)
p = (w * 4) + (tie * 2)
print(tie, p)
