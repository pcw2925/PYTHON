import datetime

now =datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

if now.hour > 12 :
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))
    
    
# 계절을 구분하는 프로그램
import datetime

now =datetime.datetime.now()

if 3 <= now.month <=5:
    print("이번 달은 {}월로 봄입니다.".format(now.month))
    
if 6 <= now.month <=8:
    print("이번달은 {} 8월로 여름입니다1".format(now.month))
    
if 9 <= now.month <=11:
    print("이번달은 {}월로 가을입니다!".format(now.month))
    
if 12 <=now.month  <=12 or 1 <= now.month <=2:
    print("이번 달은{}월로 겨울입니다!".format(now.month))
    

# 끝자리로 짝수와 홀수 구분
# 입력을 받습니다
number =input("백발백중하는 명사수")

# 마지막 자리 숫자를 추출
last_character =number[-1]

# 숫자로 변환하기
last_number =int(last_character)

# 짝수 확인
if last_number == 0 \
    or last_number ==2\
    or last_number ==4\
    or last_number ==6\
    or last_number ==8:
    print("짝수입니다") 

# 홀수 확인 
if last_number ==1 \
    or last_number ==3\
    or last_number ==5\
    or last_number ==7\
    or last_number ==9:
        print("홀수입니다")
        

# 나머지 연산자를 활용해서 짝수와 구분 
number =input("정수입력")
number =int(number)

if number %2 ==0:
    print("짝수입니다")
    

if number % 2 ==1:
    print("홀수입니다")
    
