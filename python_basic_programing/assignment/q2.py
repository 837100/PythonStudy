inputValue =  int(input("대출금액을 입력하세요 : "))


print("금리 유형별 월 이자:")
print("6개월 변동: " + str(int(inputValue * 0.0371 / 12)) + "원" )
print("12개월 변동: " + str(int(inputValue * 0.0398 / 12)) + "원" )
print("2년 고정: " + str(int(inputValue * 0.0505 / 12)) + "원")