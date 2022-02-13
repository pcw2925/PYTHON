# 날짜 시간 출력하기 
import datetime

now =datetime.datetime.now()


print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

# 날짜/시간을 한 줄로 출력하기
import datetime

now =datetime.datetime.now()

print("{}년{}월{}일{}시{}분{}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
    ))

import datetime
now =datetime.datetime.now()

if now.hour < 12:
    print("현재 시각은{}시로 오전입니다!".format(now.hour))

if now.hour >12 :
    print("현재 시각은{}시로 오후입니다!".format(now.hour))