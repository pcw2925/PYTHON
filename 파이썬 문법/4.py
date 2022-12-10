n =10
a =[0] *n
print(a)

# 리스트 인덱싱과 슬라이싱
a =[1,2,3,4,5,6,7,8,9]
# 뒤에서 첫번째 원소 출력
print(a[-1])

print(a[-3])

a[3] =7
print(a)

a =[1,2,3,4,5,6,7,8,9]

print(a[1:4])


# 리스트 컴프리핸션
# 0부터 19
array =[i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array =[i*i for i in range(1,10)]
print(array)


# N X N 크기의 2차원 리스트 초기화
n =3
m =4
array =[[0] *m for _ in range(n)]
print(array)

# N x N 크기의 2차원 리스트 초기화
n =3
m =4
array =[[0] *m] *n
print(array)

array[1][1] =5
print(array)
        