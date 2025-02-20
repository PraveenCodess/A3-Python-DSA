class student:
    name = "mew2"

    def __init__(self, name, marks):
        self.n = name
        self.m = marks
        print("default cons call")


s1 = student("mew", 45)
print(s1.n, s1.m)
s2 = student("mewboi", 87)
print(s2.n, s2.m)
