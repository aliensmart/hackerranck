class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        max_value = 0
        min_value = 101
        for i in self.__elements:
            if i < min_value:
                min_value = i
            if i > max_value:
                max_value = i
        self.maximumDifference = max_value - min_value



_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)