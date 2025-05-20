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


# 삼각형 넓이 계산 프로그램
# 넓이 1/2absinα

# GPT 피셜 : Python을 포함한 대부분의 프로그래밍 언어의 sin(), cos(), tan() 함수는 입력을 도(degree) 가 아니라 라디안(radian) 으로 받아들이기 때문입니다. 
# -> 파이썬에서 degree로 각을 표현했다면 반드시 math.radians()로 변환 후 사용
a = float(input("a의 값을 입력해주세요"))
b = float(input("b의 값을 입력해주세요"))
angle = float(input("각도가 몇° 인지 적어주세요."))

radian = math.radians(angle)
width = 1 / 2 * a * b * math.sin(radian)

print(f"삼각형 넓이 : {width}")