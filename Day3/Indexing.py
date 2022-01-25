# indexing 주소 위치를 이용해서 값에 접근하는것


from this import d

from sqlalchemy import DDL


animals =[]

animals.append('코알라')
animals.append('정상수')
animals.append('백발백중')
animals.append('좆같은공부')
animals.append('인도코끼리')

print(animals)
print(animals[4])


#  del 인덱스 값을 지울수있음
del animals[0]
print(animals)


# slicing
print(animals[0:4])


# List.sort()
animals.sort
print(animals.sort())

animals.append('인도코끼리')
print(animals)

# List.count()
print(animals.count('인도코끼리'))

del animals[1]
print(animals)

# 리스트 개수
print(len(animals))

