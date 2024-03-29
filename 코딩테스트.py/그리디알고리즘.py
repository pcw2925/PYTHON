# 탐욕 알고리즘 
# 최적의 해를 보장할 수 없을 때가 많다

# 문제
# 카운터에는 거스름 돈으로 사용할 500원 100원 50원 10원 짜리
# 동전이 무한히 존재 손님에게 거슬러 줘야할 돈이 n원 일때
# 거슬러줘야할 동전의 최소 갯수 구하기 

# 예를 들어 입력으로 주어진 n 이 1260이라면 다음과 같이 가장 큰
# 화폐 단위부터 거슬러 주는 과정을 통해 1,260원을 거슬러줄수있다

n =1260
count =0

# 큰 단위의 화폐부터 차례대로 확인
coin_types =[500,100,50,10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 새기
    n %= coin
    
print(count)

 