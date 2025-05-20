import random

options = ["가위", "바위", "보"]

while True:
    user = input("가위,바위,보 중 뭐 내실? (입력) : ")
    if user in options:
        break
    else:
        print("가위, 바위, 보 중 하나를 입력해주세요.")


com = random.choice(options)

print(f"컴퓨터가 낸 값 : {com}")
if user == com:
    print("비김")
elif user == "바위" and com == "가위":
    print("이김")
elif user == "보" and com == "바위":
    print("이김")
elif user == "가위" and com == "보":
    print("이김")
else : 
    print("짐")