# a = [1,2,3,4,5,6,7,8,9]
# print(a)

# print(a[3])

# # 크기가 n익 모든 값이 0인 1차원 리스트 초기화 
# n =10
# a =[0] *n
# print(a)

# a =[1,2,3,7,5,6,8]

# a[4] =4
# print(a)

# 슬라이싱


a =[1,2,5,5,8,9,0]
print(a[3])

print(a[1:4]) # 두번째부터 네번째 원소

# 리스트 컴프리헨션
array =[i for i in range(200)]
print(array)
# 0부터 19까지의 수 중에서 홀수만 포함하는 테스트 
array1 = [i for i in range(20) if i % 2 ==1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트 
array =[i *i for i in range(1,10)]
print(array)


array =[]
for i in range(20):
    if i % 2 ==1:
        array.append(i)
print(array)


n =4
m =3
array = [[0] * m for _ in range(n)]
print(array)

# 코드 1:1 부터 9까지 자연수를 더하기
summary =0
for i in range(1,10):
    summary += i
print(summary)

for x in range(5):
    print("Hello World")
    
# 리스트 관련 기타 메서드
a =[1,4,3]
print('기본리스트:',a)

a.append(2)
print('삽입:',a)

a.sort()
print("오름차순 정렬:" ,a)

a.sort(reverse =True)
print("내림차순 정렬:" ,a)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a =[1,2,3,4,5,5,5]
remove_set ={3,5}

# remove_list 에 포함되지 않은 값만을 저장 
result =[i for i in a if i not in remove_set]
print(result)