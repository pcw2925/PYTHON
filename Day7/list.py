# 리스트 []

# 지하철 칸별로 10명,20명, 30명

# subway1 =10
# subway2 =20
# subway3 =30;

subway =[10,20,30]
print(subway)

subway = ['정상수','백발백중','명사수']
print(subway) 

# 정상수가 몇번째 칸에 타고있는지?
print(subway.index('백발백중'))

# 값을 추가함
subway.append('정상수탈모')
print(subway)

# 정상수 백발백중 사이에 값을 넣음
subway.insert(1,'내가대표해이거리를')
print(subway)


# 한명씩 사람을 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인함 # count
subway.append('정상수')
print(subway.count('정상수'))

# 정렬
num_list = [5,4,2,7,9]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)


# 다양한 자료형 함께 사용
num_list =[5,1,2,3,4]
mix_list =['정상수',20,True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

