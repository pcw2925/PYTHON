n = int(input())
arr = [int(input()) for _ in range(n)]  # n개의 수

# 2. 선택 정렬(내림차순)
for i in range(len(arr)):
  max_idx = i  # 최댓값 인덱스
  for j in range(i + 1, len(arr)):
    # 최댓값 인덱스 갱신
    if arr[max_idx] < arr[j]:  max_idx = j
  # 최솟값 & 맨 앞 값 swap
  arr[max_idx], arr[i] = arr[i], arr[max_idx]

print(*arr)