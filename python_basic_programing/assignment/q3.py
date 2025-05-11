height = float(input("키(m)를 입력하세요 : "))
weight = float(input("몸무게(kg)를 입력하세요 : "))

bmi = weight / (height * height)

type = ""

if bmi < 18.5:
    type = "저체중"
elif bmi < 23:
    type = "정상체중"
elif bmi < 25:
    type = "과체중"
elif bmi < 30:
    type = "경도비만"
else:
    type = "고도비만"

print("BMI: " +  str(round(bmi, 2)))
print("판정 결과: " + type)



