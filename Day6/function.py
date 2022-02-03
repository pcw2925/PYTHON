from random import *

# print(random()) # 0.0이상 1.0 미만의 임의의 값을 생성
# print(random() *10) # 0.0부터 ~ 10.0 미만의 값 생성
# print(int(random() *10)) # 0~부터 10 미만의 값생성
# print(int(random() *10)) # 0~부터 10 미만의 값생성
# print(int(random() *10)) # 0~부터 10 미만의 값생성



# print(int(random() *10) +1) # 1부터 10 이하의 값생성
# print(int(random() *10) +1) # 1부터 10 이하의 값생성
# print(int(random() *10) +1) # 1부터 10 이하의 값생성
# print(int(random() *10) +1) # 1부터 10 이하의 값생성
# print(int(random() *10) +1) # 1부터 10 이하의 값생성
# print(int(random() *10) +1) # 1부터 10 이하의 값생성

# print(int(random()*45) +1)  # 1부터 45 이하의 값 생성
# print(int(random()*45) +1) 
# print(int(random()*45) +1) 
# print(int(random()*45) +1) 
# print(int(random()*45) +1) 
# print(int(random()*45) +1) 

# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))

# print(randint(1,45)) # 1부터 45까지 포함
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))

# quiz 
# 월 4회 스터디를 하는데 3번은 온라인 1번은 오프라인
# 조건1 랜덤으로 날짜를 뽑아야함
# 조건2 월별~날짜는 다름을 감안하여 28일 이내로 정함
# 조건3 매월 1~3일은 스터디 준비를 해야하므로 제외

data =randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" 
      +str(data) +" 일로 선정되었습니다")