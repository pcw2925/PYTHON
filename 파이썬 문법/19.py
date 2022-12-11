# 투포인터
# 리스트에 순차적으로 접근해야할때 2개의 점 위치를 기록하면서 처리하는 알고리즘
n =5
m =5
data=[1,2,3,2,5] # 전체 수열

count =0
interval_sum =0
end =0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end +=1
    # 부분 합이 m일때 카운트 증가
    if interval_sum == m:
        count +=1
    interval_sum -= data[start]
print(count)