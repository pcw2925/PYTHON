from tkinter import E


array =[]

for i in range(0,20,2):
    array.append(i *i)
print(array)

# 리스트 안에 for 문 사용하기
array =[i *i for i in range(0,20,2)]
print(array)

# 조건을 활용한 리스트 내포
array =['사과','자두','초콜릿','바나나','빈대떡']
output =[fruit for fruit in array if fruit != "바나나"]
print(output)    

# if 조건문과 여러 줄 문자열 
number = int(input("정상수 입력"))

if number % 2 ==0:
    print("""입력한 문자열은 {} 입니다.
{}는  짝수입니다.""".format(number,number))
else:
    print("""입력한 문자열은{} 입니다
{} 는 홀수 입니다.""".format(number,number))
    
# if 조건문과 긴 문자열
number = int(input("정수입력"))

if number % 2 == 0:
    print("입력한 문자열은 {}입니다. \n{}는 짝수입니다.".format(number.number))
else:
    print("입력한 문자열 {}은입니다\n{}홀수입니다.".format(number,number))
    
    
# 괄호로 문자열 연결하기
test = (
    "이렇게 연결해도"
    "정상수 벡발백중"
    "정상수 탈모"
)
print("test:",test)
print("type(test):",type(test))

# 여러줄 문자열과 if 구문을 조합
number =int(input("정상수입력"))

if number % 2 == 0:
    print((
        "입력한 문자열은 {} 입니다.\n"
        "{}는 짝수 입니다."
    ).format(number,number))
else:
     print((
        "입력한 문자열은 {} 입니다.\n"
        "{}는 홀수 입니다."
    ).format(number,number))