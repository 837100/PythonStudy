# 프로그래밍은 똑같은 일을 반복하지 않도록 다양한 구조와 개념을 제공

# msg = "저는 파이썬을 잘 다룰 수 있습니다."
# count = 0
# while count < 5:
#     print(msg)
#     count = count + 1

# sum = 0
# i = 1
# num = int(input("어디까지 더할까요? : "))
# while i <= num:
#     sum = sum + i
#     i = i + 1
# print(sum)

# # 구구단
# base_num = int(input("출력할 단을 입력하세요"))
# for x in range(1, 10):
#     print(base_num, "*", x, "=", base_num * x)

# base = int(input("출력할 단을 입력하세요: "))
# i = 1
# while i <= 9:
#     print(base, "X", i, "=", base * i)
#     i += 1

# List - 리스트
# 객체(object)는 객체지향 프로그램에서 모든 것을 의미함.
"""
인덱스 연산자 시퀀스 타입의 원소에 접근하는 연산자
"""

rad = 10
hei_list = [1, 5, 14, 26, 31]

for hei in hei_list:
    vol = 1 / 3 * 3.14 * rad**2 * hei
    surf = 3.14 * rad**2 + 3.14 * rad * hei
    print("원뿔의 부피는", vol, "입니다.")
    print("원뿔의 겉넓이는", surf, "입니다.")
