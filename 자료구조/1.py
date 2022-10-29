# menu ={'커피','우유','주스'}
# print(menu,type(menu))

# menu =list(menu)
# print(menu,type(menu))

# menu =tuple(menu)
# print(menu,type(menu))

# menu =set(menu)
# print(menu,type(menu))

# # 퀴즈
# from random import *
# users =range(1,21)
# # print(type(users))
# users =list(users)
# # print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners =sample(users,4)

# print('당첨자 발표')
# print("치킨 당첨자: {0}".format(winners[0]))
# print("커피당첨자 : {0}".format(winners[1:]))
# print('축하합니다')

# # if문
# weather =input("오늘 날씨는 어때요?")
# if weather =="비":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요 나가지마세요")
# elif 10 <= temp and temp< 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp <10:
#     print('외투를 챙기세요')
# else:
#     print("너무 추워요 나가지마세요")

# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

for waitting_no in range(1,6):
    print("대기번호: {0}".format(waitting_no))
    
