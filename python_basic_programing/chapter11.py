import math
from math import sin


# dir(math)
# help(math.gamma)


class Cone:
    def __init__(self, radius=20, height=30):
        self.r = radius
        self.h = height

    def get_vol(self):
        return 1 / 3 * math.pi * self.r ** 2 * self.h

    def get_surf(self):
        return math.pi * self.r ** 2 + math.pi * self.r * self.h


# math 모듈
# 수학적 계산 문제를 해결하기 위한 수학 함수 및 상수의 집합.

# random 모듈
# 난수를 만들 때 굉장히 만들 때 사용.


a, b = 10, 20
area = 1 / 2 * a * b * sin(math.radians(60))
print(area)
