# print(list(range(10)))


# # 매개변수에 숫자를 두 개 넣은 범위
# print(list(range(0,5)))

# print(list(range(5,10)))

# # 맨 끝자리수를 포함
# a =range(0,10 +1)
# print(list(a))

# n= 10
# a = range(0,n/ 2) # 매개변수로 나눗셈을 사용해서 오류 발생 
# print(a)

# a =range(0,int(n / 2))
# print(list(a))

# a =range(0,n //2)
# print(list(a))


# 반복문과 범위
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5,10):
    print(str(i) +"= 반복 변수")
print()

for i in range(0,10,3):
    print(str(i)  + "=반복 변수")
print()

# 리스트와 범위를 조합해서 사용하기
array =[273,32,103,57,52]

# 리스트에 반복문을 적용 
for i in range(len(array)):
    # 출력 
    print("{} 번째 반복: {}".format(i,array[i]))
    
# 반대로 반복하기
for i in range(4,0 -1,-1):
    # 출력합니다
    print("현재 반복 변수: {}".format(i))
    
# reversed 함수 사용 
for i in reversed(range(5)):
    print("현재 반복상수 변수: {}".format(i))
    
# while 반복문
# while True:
#     print("check this out 나는 정상수")

# while for 반복문 처럼 사용하기
i = 0
while i < 10: # 9번까지 반복  
    print("{}번째 반복입니다.".format(i))
    i +=1
    
# remove 상태를 기반으로 반복하기
# 해당하는 값 모두 제거하기
list_test =[1,2,1,2]
value =2

while value in list_test:
    list_test.remove(value)
print(list_test)
# 리스트 내부에 있는 모든 2가 제거 될때까지 반복 2가 모두 제거


# while 반복문 시간을 기반으로 반복하기
# import time
# print(time.time()) # 유닉스 타임 

# 시간과 기능을 가져옵니다
# import time

# # 변수 선ㅇㄴ 
# number =0

# # 5초동안 반복 
# target_tick =time.time() +5
# while time.time() < target_tick:
#     number += 1

# # 출력         
# print("5초 동안 {}번 반복 했습니다.".format(number))


# while 반복문 : break /continue
# 변수를 선언
i = 0
while True:
    print("{}번째 반복문입니다".format(i))
    i = i +1
    
    input_text =input("종료 하시겠습니까?(y/n):")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다")
        break
    
# continue 
numbers =[5,15,6,20,8,25]

for number in numbers:
    if number <10: # 10보다 작으면 다음 반복으로 넘어감 
        continue
    print(number)