print('   *')
print('  ***')
print(' *****')
print('*******')

line = int(input('몇 줄을 생성 하실 건가요?'))
empty = line - 1
star = 1
for i in range(line):
    for j in range(empty):
        print(' ', end='')
    empty -= 1
    for j in range(star):
        print('*', end='')
    star += 2
    print()

# 파이썬은 문자열에 *숫자로 반복 생성 가능.
print('간단한 for문')
for i in range(line):
    print(' ' * (line - i - 1) + '*' * (2 * i + 1))


# 사용자의 입력은 모두 문자열로 들어옴.
# 반지름 사용자 입력
rad = int(input('반지름을 입력하세요:'))
# 높이 사용자 입력
hei = int(input('높이를 입력하세요:'))
# 부피& 겉넓이 계산
vol = 1 / 3 * 3.14 * rad ** 2 * hei
suf = 3.14 * rad ** 2 + 3.14 + rad * hei
print('부피의 값: ',vol,sep='기본값은 한 칸 띄워지지만(공백 문자열) sep(seperate)로 지정 가능')
print('겉 넓이의 값: ',suf,sep='')
