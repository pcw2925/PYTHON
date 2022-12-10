# 내장함수
result =sum([1,2,3,4,5])
print(result)

result =min(7,3,5,2)
print(result)

result =max(12,45551,678,1241)
print(result)

result =eval("(3+5)*7")
print(result)

result =sorted([9,1,8,5,4]) # 오름차순 정렬
print(result)

result =sorted([9,1,8,5,4],reverse =True) # 내림차순 정렬
print(result)

result =sorted([('홍길동',35),('이순신',75),('정상수',15)],
               key =lambda x: x[1],reverse=True)
print(result)


# 오름차순
data =[91,635123,2636,12767]
data.sort()
print(data)


