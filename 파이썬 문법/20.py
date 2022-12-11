# 두리스트의 합집합
n,m=3,4
a= [1,3,5]
b= [2,4,6,8]

result =[0] *(n+m)
 
i=0
j=0
k=0
 
 # 모든 원소가 결과 리스트에 담길때 까지 반복
while i < n or j < m:
    # 리스트 b의 모든 원소가 처리되었거나 리스트  a 의 원소가 더적을때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 a의 원소를 결과 리스트로 옮기기
        result[k] =a[i]
        i += 1
        # 리스트  a의 모든 원소가 처리되었거나 리스트 b의 원소가 더적을때
    else:
        # 리스트 b의 원소를 결과 리스트로 옮기기
        result[k] =b[j]
        j +=1
    k += 1
# 결과 리스트 출력
for i in result:
    print(i,end='')
