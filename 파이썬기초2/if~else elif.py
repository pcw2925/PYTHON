number =input("정상수입력")
number = int(number)

if number % 2 ==0:
    print("짝수입니다")
if number % 2 ==1:
    print("홀수입니다 ")


number =input("정수 입력")
number =int(number)

if number %2 ==0:
    print("짝수입니다")
else:
    print("홀수입니다")
    

import datetime

now = datetime.datetime.now()
month =now.month

if 3 <= month <=5:
    print("현재는 봄입니다")
elif 6 <= month <=8:
    print("현재는 여름입니다")
elif 9 <= month <11:
    print("현재는 가을입니다")
else:
    print("겨울입니다 ")
    

# 조건문 구현
score =float(input("학점 입력"))

if score == 4.5:
    print("신")
elif 4.2 <= score <4.5:
    print("정상수")
elif 3.5 <= score <4.2:
    print("백발백중")
elif 2.8 <= score <3.5:
    print("명사수")
elif 0<= score <2.8:
    print("정상수두피")
    

# False로 변환되는 값
print("# if 조건문에 0 넣기")
if 0:
    print("0은 Trueㄹ 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")
    
# pass 사용법
# 입력을 받습니다
number =input("정수입력")
number = int(number)

if number > 0:
    # 양수일때: 아직 미구현
    pass
else:
    # 음수일 때 :아직 미구현 상태입니다
    pass 