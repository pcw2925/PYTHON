n =int(input())

ugly =[0] *n
ugly[0] =1

# 2배,3배 ,5배를 위한 인덱스
i2 =i3 =i5 =0
next2,next3,next5=2,3,5

# 1부터 n 까지의 못생긴 수를 찾기
for I in range(1,n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[1] =min(next2,next3,next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[1] ==next2:
        i2 +=1
        next2 =ugly[i2] *2
    if ugly[1] == next3:
        i3 +=1
        next3 =ugly[i3] *3
    if ugly[1] ==next5:
        i5 +=1
        next5 =ugly[i5] *5
        
print(ugly[n-1])