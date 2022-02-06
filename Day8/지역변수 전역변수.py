# gun =100 # 지역변수 

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun -soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
    
    
# def checkpoint_ret(gun,soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun 


# print("전체 총: {0}" .format(gun))
# # checkpoint(4) # 2명이 경계근무 나감

# gun =checkpoint_ret(gun,10)
# print("남은 총 : {0}".format(gun))


# quiz

def std_weight(height,gender): # 키는 m단위 (실수) ,성별 '남자 '여자
    if gender == '정상수':
        return height * height *22
    else:
        return height * height *21
    
height =  175 # cm
gender = "정상수"
weight = round(std_weight(height / 100, gender),2)
print(" 키 {0} cm {1} 의 표준 체중은 {2} kg 입니다".format(height,gender,weight))