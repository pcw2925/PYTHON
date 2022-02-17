numbers =[103,52,273,32,77]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# reversed() 함수
list_a =[1,2,3,4,5]
list_reversed =reversed(list_a)

print("# reversed() 함수")
print("reversed([1,2,3,4,5]):",list_reversed)
print("list(reversed([1,2,3,4,5)):", list(list_reversed))
print()     


print("# reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-", i)
    


# temp
temp =reversed([1,2,3,4,5,6])

for i in temp:
    print("첫 번째 반복문:{}".format(i))
    
for i in temp:
    print("두 번째 반복문: {}".format(i))

#  reversed 함수의 결과가 제너레이터이기 때문에
#  첫 번째 반복문만 실행됨

number =reversed([1,2,3,4,5,6])

for i in reversed(numbers):
    print("첫 번째 반복문:{}".format(i))
    
for i in reversed(numbers):
    print("두 번째 반복문: {}".format(i))


# 확장 슬라이싱
numbers =[1,2,3,4,5]

numbers[::-1]
print(numbers)


# enumerate 함수와 반복문 조합하기
example_list =["정상수A",'정상수B','정상수C']
i =0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i,item))
    i +=1
    
# enumerate () 함수와 리스트
example_list =['정상수A','정상수B','정상수C']

print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수를 적용해 출력합니다
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list 함수로 강제 변환해 출력합니다
print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print('# 반복문과 조합하기')
for i, value in enumerate(example_list):
    print("{} 번째 요소는 {} 입니다.".format(i,value))
    
# 딕셔너리의 items() 함수와 반복문
exmaple_dictionary ={
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print("# 딕셔너리의 items() 함수")
print("item():",exmaple_dictionary.items())
print()

# for 반복문과 items() 함수 조립해서 사용하기
print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in exmaple_dictionary.items():
    print("dictionary[{}]) ={}".format(key,element))