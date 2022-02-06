# 출석 번호 1,2,3,4, 앞에 100을 붙이기로함
# students =[1,2,3,4,5]
# print(students)

# students =[i+100 for i in students]
# print(students)


# 학생 이름을 길이로 변환
students =['jeongsangsu','정상수','정상수1','정상수2' ]
students =[len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환 
students =['jeongsangsu','정상수','정상수1','정상수2' ]
students =[i.upper() for i in students]
print(students)


# quiz

from random import *
cnt =0
for i in range(1,51): #  1부터 50 이라는 수 (승객)
    time = randrange(5,51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분에서 ~ 15분 이내의 손님 ,탑승수 증가처리
        print("[0] {0} 0번째 손님(소요시간: {1}분)".format(i,time))
        cnt +=1
    else: # 매칭 실패한 경우
         print("[] {0} 0번째 손님(소요시간: {1}분)".format(i,time))
print("총 탑승 승객: {0} 분".format(cnt))