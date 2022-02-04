# 내용 변경 추가 불가능 속도가 리스트보다 빠름

menu =('정상수','치즈정상수')

print(menu[0])
print(menu[1])

# 튜플은 add 사용 불가능 
# menu.add('백발백중정상수')

# name ="최종명"
# age =20
# hobby ="ㅅㅂ놈"
# print(name,age,hobby)

(name,age,hobby) =('정상수',20,'코딩')
print(name,age,hobby)

# quiz
def std_weight(height,gender):  # m 단위
    if gender =="남자":
        return height *height *22
    else:
        return height *height *21

height = 175  #cm 단위
gender ='남자'
weight =round(std_weight(height /100 ,gender),2)
print("키 {0}cm {1} 의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))