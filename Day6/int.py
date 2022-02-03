# 숫자 맟추기 게임 !!! 
import random as rd

import random

print("숫자 맟추기 게임")

choice =random.randrange(100)
print(choice)

while True:
    
    user_choice =int(input('100보다 작은정상수를 입력하세요'))
    
    if choice == user_choice:
        break;
    
    if choice < user_choice:
        print('값이 너무큽니다')
    else:
        print('입력한 값이 너무 낮아요 ')
    
print('정답입니다 프로그램을 종료합니다')
