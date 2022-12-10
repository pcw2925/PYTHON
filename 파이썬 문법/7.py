data =dict()
data['사과'] ='Apple'
data['바나나'] ='Banana'
data['코코넛'] ='Cocount'

print(data)

data =dict()
data['사과'] ="Apple"
data['바나나'] ='Banana'
data['코코넛'] ='Cocount'

if'사과' in data:
    print("사과를 키로 가지는 데이터가 존재합니다")
    
# 사전 자료형 관련 함수
data =dict()
data['사과'] ="Apple"
data['바나나'] ='Banana'
data['코코넛'] ='Cocount'

# 키 데이터만 담은 리스트
key_list =data.keys()
# 값 데이터만 담은 리스트
value_list=data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])    

# 집합 자료형
# 중복허용 x
# 순서 x
# 집합 자료형 초기화 방법1
data =set([1,1,2,3,4,4,5])
print(data)

# 집합 자료형 초기화 방법 2
data ={1,1,2,3,4,4,5}
print(data)

# 집합 자료형의 연산
a =set([1,2,3,4,5])
b= set([3,4,5,6,7])

print(a | b)
print(a&b)
print(a-b)

# 집합 자료형 관련 함수
data =set([1,2,3])
print(data)

data.add(4)
print(data)

# 새로운 원소 여러개 추가
data.update([5,6])
print(data)