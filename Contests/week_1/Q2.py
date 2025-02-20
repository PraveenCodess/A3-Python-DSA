# Given three angles of a triangle, determine whether it is an acute,
# obtuse, or right-angled triangle.


def triangle(n1, n2, n3):
    if n1 < 90 and n2 < 90 and n3 < 90:
        print("Acute")
    if n1 > 90 or n2 > 90 or n3 > 90:
        print("Obtuse")
    if n1 == 90 or n2 == 90 or n3 == 90:
        print("Righr-angled triangle")


triangle(80, 50, 50)
