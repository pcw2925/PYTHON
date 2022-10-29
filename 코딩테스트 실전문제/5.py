# 볼링공 가르기
# split 문자열.split(sep, maxsplit) 함수는 문자열을
# maxsplit 횟수만큼 sep의 구분자를 기준으로 문자열을 구분하여 잘라서 리스트로 만들어 줍니다.

n,m =map(int,input().split())

data =list(map(int,input().split()))

array =[0] *11
for x in data:
    array[x] +=1
# 1부터 m까지의 각 무게에 대하여 처리
result =0

for i in range(1,m+1): # 무게가 i인 볼링공의 개수 제외
    n -=array[i] 
    result +array[i] * n # b가 선택하는 경우의 수와 곱하기
print(result)
