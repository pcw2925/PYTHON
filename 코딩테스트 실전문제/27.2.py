from bisect import bisect_left,bisect_right

def count_by_range(array,left_value,right_value):
    right_index =bisect_right(array,right_value)
    left_index =bisect_left(array,left_value)
    return right_index -left_index

n,x=map(int,input().split()) # 데이터의 개수 n 찾고자 하는 값 x를 입력받기
array=list(map(int,input().split()))

# 값이 [x,x] 범위에 잇는 데이터의 개수 개산
count =count_by_range(array,x,x)
# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
           