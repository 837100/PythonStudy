'''
반환 값이 없는 함수
def 함수이름(배개변수 리스트):
    명령 블록
'''
from os import minor


# 원뿔 계산 함수 정의
def prt_cone_vail(r, h):
    if r > 0 and h > 0:
        vol = 1 / 3 * 3.14 * r ** 2 * h
        print('월뿔의 부피는', vol, '입니다.')
    else:
        print('반지름과 높이 값에 양수를 입력하세요')


rad = 30
hei = 50
prt_cone_vail(rad, hei)

# 숫자 역순 출력 프로그램
# 숫자를 입력받고 역순으로 출력하는 함수를 사용한 프로그램을 작성하시오

input_string = input('텍스트를 입력하세요 ([,]으로 나눠주세요)').split(',')
print(input_string)
convert_int = []

for i in range(len(input_string)):
    try:
        convert_int.append(int(input_string[i]))
    except ValueError:
        continue

print('정수로 변환', convert_int)


tmp = 0
for i in range(len(convert_int) - 1):
    max_val = i
    for j in range(i+1, len(convert_int)):
        if convert_int[j] > convert_int[max_val]:
            max_val = j
            convert_int[i] , convert_int[max_val] = convert_int[max_val], convert_int[i]
print('정렬 결과', convert_int)
