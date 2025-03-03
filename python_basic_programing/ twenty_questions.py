import random

hit_number = random.randint(1, 10)
count = 0

is_pass = False

while count < 20:
    guess = int(input("숫자를 맞혀보세요(" + str(count+1) + ")번째): "))
    if hit_number == guess:
        is_pass = True
        print("맞아요! 정답은 " + str(hit_number) + "입니다.")
        break
    elif hit_number > guess:
        print(str(guess) + "보다 큽니다.", end="")
        count += 1
    else:
        print(str(guess) + "보다 작습니다.", end="")
        count += 1

if is_pass == False: print('실패!')
