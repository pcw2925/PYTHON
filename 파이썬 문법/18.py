# 에라토스테네스의 체 알고리즘
import math

n =1000
array =[True for i in range(n+1)] # 처음엔 모든 수가 소수인 것으로 초기화
for i in range(2,int(math.sqrt(n)) +1): # 2부터 n의 제곱근 까지의 모든수를 확인
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i *j <= n:
            array[i*j] =False
            j +=1
# 모든 소수를 출력
for i in range(2,n+1):
    if array[i]:
        print(i,end='')
        
