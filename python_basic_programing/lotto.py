import random

guess_str = input("1~45 번호 6개를 쉼표로 분리하여 입력하세요: ").split(",")
guess_list = list()

for i in guess_str:
    guess_list.append(int(i))

lotto_list = random.sample(range(1, 46, 1), 6)
# print에서 여러 인수를 받아 출력할 때 문자열과 리스트는 +로 연결 할 수 없음
print("예상 번호는" , guess_list, "입니다.")
print("추첨 번호는", lotto_list, "입니다.")

hit_count = 0;

for i in guess_list:
    if i in lotto_list:
        hit_count = hit_count + 1

print("축하합니다." + str(hit_count) + "개 맞혔습니다.")
