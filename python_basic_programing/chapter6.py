# rad = 0
# hei = 0

rad = int(input("반지름을 입력하세요:"))
hei = int(input("높이를 입력하세요:"))

if rad > 0 and hei > 0:
    vol = 1 / 3 * 3.14 * rad ** 2 * hei
    suf = 3.14 * rad ** 2 + 3.14 * rad * hei
    print("원뿔의 부피는", vol, "입니다.")
    print("원뿔의 겉넓이는", suf, "입니다.")
else:
    print("반지름과 높이의 값을 모두 양수로 입력해주세요.")

temp = 20
fruit = "apple"
print(temp >= 27 and fruit == "pear")

A = int(input("A 입력: "))
B = int(input("B 입력: "))
C = int(input("C 입력: "))

print(max(A, B, C))
if A > B:
    if A > C:
        print(A)
    else:
        print(C)
else:
    if B > C:
        print(B)
    else:
        print(C)

if A > B and A > C:
    print(A)
elif B > A and B > C:
    print(B)
elif C > A and C > B:
    print(C)

if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else:
    print(C)
