array =[3,5,1,2,4,1,2,3,5,7,8,9,0] # n 개의 데이터
summary =0 # 합계를 저장할 변수

for x in array: # 모든 데이터를 하나식 사용하여 합계
    summary += x
# 결과를 출력 
print(summary)

array =[3,5,1,2,4]

for i in array:
    for j in array:
        temp =i *j
        print(temp)
        
        
# 수행 시간 측정 코드
import time
start_time =time.time()

end_time =time.time()
print("time :" ,end_time -start_time)

# 선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교
from random import randint
import time
#  배열에 10,000개의 정수를 삽입 
array =[]
for x in range(10000):
    array.append(randint(1,100))
# 선택 정렬 프로그램 성능 측정 
start_time =time.time()

# 선택 정렬 프로그램 소스코드 
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스 
    for j in range( i +1, len(array)):
        if array[min_index] > array[j]:
            min_index =j
    array[i],array[min_index] =array[min_index], array[i]
    
    end_time =time.time() # 측정 종료 
    print("선택 정렬 성능 측정:" ,end_time -start_time) # 수행 시간 출력 

# 베열을 다시 무작위 데이터로 초기화 
array =[]
for x in range(10000):
    array.append(randint(1,100))

# 기존 정렬 라이브러리 성능 측정 
start_time =time.time()
# 기본 정렬 라이브러리 사용 
array.sort()

end_time =time.time() # 측정 종료 
print("기본 정렬 라이브러리 성능 측정:" ,end_time -start_time) # 수헹 시간 출력 