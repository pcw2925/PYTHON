# starbucks =["아이언맨",'토르','아이엠 그루트']
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# while
# customer = "토르"
# index =5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. 호출{1}회".format(customer,index))
#     index -= 1
#     if index == 0:
#         print('커피는 폐기처분 되었습니다')    

# customer ="아이언맨"
# index =1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1}회".format(customer,index))
#     index += 1

# customer ='토르'
# person ="Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person =input("이름이 어떻게 되세요?")
    

# absent =[2,5] #결석
# no_book =[7] # 책을 깜빡한남자
# for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐.".format(student))
    
# 한줄 for문 
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로함 -> 101,102,103,104 
# students =[1,2,3,4,5]
# print(students)
# students =[i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students =['Iron man','thor',' i am 오석진']
# students =[len(i) for i in students]
# print(students)

    
    
# # 학생 이름을 대문자로 변환 
# students =['Iron man','thor',' i am 오석진']
# students =[i.upper() for i in students]
# print(students)

# 승객과 매칭 기회 총 탑승 승객 수를 구하는 프로그램
from operator import contains
from random import *
cnt =0
for i in range(1,51): # 1부터 50
    time =randrange(5,51) # 5분 ~ 50분 소요
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님, 탑승 수 증가 처리
        print("[0] {0}번째 손님 (소요시간:{1}분)".format(i,time))
        cnt +=1
    else:
         print("[ ] {0}번째 손님 (소요시간:{1}분)".format(i,time))

print("총 탑승 승객:{0} 분".format(cnt))

    
         
        
        
        
    