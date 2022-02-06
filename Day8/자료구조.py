# 자료구조의 변경
menu ={"커피",'우유','주스'}
print(menu,type(menu))

menu =list(menu)
print(menu,type(menu))

menu =tuple(menu)
print(menu,type(menu))

menu =set(menu)
print(menu,type(menu))

# quiz
# from random import *
# # list =[1,2,3,4,5]
# print(list)
# shuffle(list)
# print(list)
# print(sample(list,1))


from random import *
users =range(1,21) # 1부터 20까지 숫자 생성
# print(type(users))
users =list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users,4) # 4명중에 한명은 치킨 1명은 정상수와 키스
print(" --- 당첨자 발표 --")
print("치킨 당첨자: {0}".format(winners[0]))
print("정상수와 키스권 당첨자: {0}".format(winners[1:]))
print("------축하합니다----")
