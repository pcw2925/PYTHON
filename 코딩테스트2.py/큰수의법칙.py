test = [2, 4, 5, 4, 6]

m = 8  # 개수 제한
k = 3  # 반복 개수 제한

# 가장 큰 수
max_value = max(test)

# 가장 큰수 제거
test.pop(test.index(max_value))
print(test)

# 가장 큰수가 제거된 리스트에서 가장 큰 수 (처음 리스트의 두번째 큰 수)
max_second = max(test)

result = 0

# k 를 담은 변수 선언
copy_k = k

for i, v in enumerate(range(m)):
    # 가장큰 수를 k번 더했을때 두번째로 가장 큰 수를 더하고 copy_k 를 다시 k로 셋팅
    if copy_k == 0:
        result += max_second
        copy_k = k
    else:
        # 가장 큰 수를 더한다.
        result += max_value
        copy_k = copy_k - 1


print(result)

# 정답코드

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수 정렬

first = data[n - 1]  # 마지막 원소 = 제일 큰 수
second = data[n - 2]  # 두번째로 큰 수 = 마지막에서 두번재 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)


result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두번째로 큰 수 더하기

print(result)