from collections import deque

data =deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 변환

from collections import Counter
counter =Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) # blue가 등장한 횟수 출력
print(counter['green']) # green 이 등장한 횟수 출력
print(dict(counter))

# math 라이브러리
# 팩토리얼 제곱근 최대공약수 계산
# math 라이브러리의  factorial (x) 함수는 x! 값을 반환

import math
print(math.factorial(5)) # 5팩토리얼을 출력

import math
print(math.sqrt(7)) # 7의 제곱근 출력

import math
print(math.gcd(21,14)) # 21과 14의 최대공약수 출력

import math
print(math.pi) # 파이 출력
print(math.e) # 자연 상수 e 출력

