array =[273,32,103,'문자열',True,False]
print(array)

list_a =[273,32,103,'문자열',True,False]
print(list_a[0])

print(list_a[1:3])

list_a = [273,32,103,'문자열',True,False]
list_a[0] ="정상수"
print(list_a)

list_a =[273,32,103,'문자열',True,False]
print(list_a[-1])


list_a =[273,32,103,'문자열',True,False]
print(list_a[-2])

list_a =[[1,2,3],[4,5,6],[7,8,9]]
print(list_a[1])

print(list_a[1][1])

# list_a =[273,32,103]
# print(list_a[3])

list_a =[1,2,3]
list_b =[4,5,6]

print("# 리스트")
print("list_a =", list_a)

print("list_b =",list_b)
print()

print("# 리스트 기본 연산자")
print("list_a +list_b=", list_a +list_b)
print("list_a * 3 =",list_a *3)
print()

print("# 길이 구하기")
print("len(list_a) =",len(list_a))

# 리스트에 요소 추가하기 :append,insert
list_a =[1,2,3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("#리스트 중간에 요소 추가하기")
list_a.insert(0,6)
print(list_a)

# extend 매개변수로 리스트를 입력 원래 리스트 뒤에 새로운 리스트
# 요소를 모두 추가 해줍니다 
list_a =[1,2,3]
list_a.extend([4,5,6])
print(list_a)

list_a =[1,2,3]
list_b =[4,5,6]
list_a.extend(list_b)
print(list_a)
print(list_b)

# 리스트에 요소 제거하기
list_a =[0,1,2,3,4,5,6,7]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법[1]
del list_a[1]
print("del list_a[1]:",list_a)

# 제거 방법[2]
list_a.pop(2)
print("pop(2):",list_a)

list_b= [0,1,2,3,4,5,6]
del list_b[3:6] # 3번부터 5번째까지 지움
print(list_b)

list_c =[0,1,2,3,4,5,6]
del list_c[:3] # 3번째 불포함으로 왼쪽을 모두제거
print(list_c)

list_d =[0,1,2,3,4,5,6]
del list_d[3:] # 3을기준 3번째 포함 오른쪽을 모두 제거 
print(list_d)

# 값으로 제거하기 :remove
list_c =[1,2,1,2] # 리스트 선언
list_c.remove(2)  # 리스트의 요소를 값으로 제거하기 
print(list_c)

list_d =[0,1,2,3,4,5]
list_d.clear()
print(list_d)

# 리스트 내부에 있는지 확인
list_a =[273,32,103,56,52]
print(273 in list_a)

print(273 not in list_a)

