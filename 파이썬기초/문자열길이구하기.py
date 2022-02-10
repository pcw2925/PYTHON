from html.entities import name2codepoint


print(len("정상수입니다"))

# 숫자
# 소수점이 없는 숫자를 정수형이라고하고 소수점이 있으면 실수형
print(type(273))
print(type(52.284))

# int integer :정수
# float : 부동 소수점 실수
print(0)
print(type(0))

print(0.0)
print(type(0.0))


# 숫자 연산자
print("5 +7 =",5+7)
print("5 -7=",5-7)
print("5 *7" ,5*7)
print("5/7=", 5/7)

# 나누기 연산자
print("3 /2=", 3/2)
print("3 // 2==", 3 // 2)
print("5 % 2=" ,5 % 2) 


print("2 ** 1 =", 2**1)
print("2 ** 2 =", 2 **2)
print("2 ** 3 =", 2*3)
print("2 ** 4 =", 2**4)


print(5 +3 *2)


# 변수 만들기/사용하기
pi =3.14159256
print(pi)

pi =3.14159265
print(pi +2)
print(pi -2)
print(pi *2)
print(pi /2)
print(pi *pi)

# 원의 둘레와 넓이 구하기
pi =3.1459265
r =10

print("원주율 =" ,pi)
print("반지름 =",r)
print("원의 둘레 =",2*pi*r)
print("원의 둘레 =",pi*r*r)

# 복합 대입 연산자
# += 숫자 덧셈후 대입
# -= 숫자 뺄셈후 대입
# * = 숫자 곱셈후 대입
# /= 숫자 나눗셈후 대입
# % = 숫자의 나머지를 구한후 대입
# ** = 숫자 제곱후 대입 

number =100
number +=40
number -=20
number +=30
print("number:" ,number)

# 문자열
# += 문자열 연결후 대입
# *= 문자열 반복후 대입 


# input() 함수로 사용자 입력받기
# string =input("정상수를 입력하세요")
# print(type(string))

# number =input("숫자를 입력하세요")
# print(type(number))


# # 입력 자료형 확인하기
# string =input("입력> ㅈ")

# print("자료:" ,string)
# print("자료형:" ,type)


# # 입력받고 더하기
# string = input("입력>")

# 출력
# print("입력 +100:" ,string +100) # 문자열과 숫자는 더할수 없어서 오류


# int() 함수 사용하기
string_a =input("입력A>" )
int_a =int(string_a)

string_b =input('입력B >')
int_b =int(string_b)

print("문자열 자료:" ,string_a +string_b)
print("숫자 자료:" ,int_a +int_b)

# int() 함수와 float() 함수 활용하기
output_a =input('52')
output_b =float("52.274")

print(type(output_a), output_a)
print(type(output_b), output_b)


# int 함수와 float 함수 조합하기
input_a =int(input("첫번째 숫자 >"))
input_b =int(input("두번째 숫자 >"))

print("덧셈 결과:", +input_a +input_b)
print("뺄셈결과:" ,input_a -input_b )
print("곱셈결과:" , input_a *input_b)
print("나눗셈 결과:", input_a /input_b)

# format 함수
