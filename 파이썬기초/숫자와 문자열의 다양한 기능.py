# format 문자열이 가지고 있느 함수

string_a ="{}".format(10)

print(string_a)
print(type(string_a))

# format() 함수로 숫자를 문자열 변환하기
# 매개변수가 많으면 인덱스 오류 발생 
format_a ="{}만 원.".format(5000)
format_b ="파이썬 열공하여 첫 연봉 {}만 원 만들기".format(50000)
format_c ="{} {} {}".format(3000,4000,5000)
format_d ="{} {} {}".format(1,'문자열',True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)


# 정수를 특정 칸에 출력하기
output_a = "{:d}".format(52)
output_b = "{:5d}".format(52) # 5칸을 잡고 뒤에서 52숫자채움
output_c ="{:10d}".format(52) # 10칸을 잡고 뒤에서 52 숫자채움
output_d ="{:05d}".format(52) # 5칸을 잡고 앞의 빈곳을 0으로채움
output_e ="{:05d}".format(52) # 부호가 있을땐 앞자리를 부호로채움 빈곳을 0으로 채움

print('기본')
print(output_a)
print('특정 칸에 출력하기')
print(output_b)
print(output_c)
print('# 빈칸을 0으로 채우기')
print(output_d)
print(output_e)


# 기호 붙여 출력하기
output_f ="{:+d}".format(52)
output_g ="{:+d}".format(-52)
output_h ="{: d}".format(52)
output_i ="{: d}".format(-52)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)

# 정수 출력을 조합하기
output_h ="{:+5d}".format(52)
output_i ="{:+5d}".format(-52)
output_j ="{:=+5d}".format(52)
output_k ="{:=+5d}".format(-52)
output_l ="{:+05d}".format(52)
output_m ="{:+05d}".format(-52)

print('#조합하기')
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)

# float 자료형 기본
a ="{:f}".format(52.645)
b ="{:15f}".format(52.645) # 15칸 만들기
c ="{:+15f}".format(52.645) # 15칸에 부호추가하기
d ="{:+015f}".format(52.645) # 15칸에 부호 추가하고 0으로 채움

print(a)
print(b)
print(c)
print(d)

# 소수점 아래 자릿수 지정하기
output_a ="{:15.3f}".format(52.274) # 15칸을 잡고 소수점 3자리출력
output_b ="{:15.2f}".format(52.274) # 15칸을 잡고 소수점 2자리출력
output_c ="{:15.1f}".format(52.274) # 15칸을 잡고 소수점 1자리출력

# 소수점 제거하기
output_a =52.0
output_b ="{:g}".format(output_a) # :g 소수점 제거 
print(output_a)
print(output_b)


# 대소문자 바꾸기 upper()와 lower()

a= 'Hello python Programming'
print(a.upper()) # 대문자로바꿈
print(a.lower()) # 소문자로바꿈 


# 문자열 양옆의 공백 제거하기 :strip()
# strip # 문자열 양옆의 공백 제거
# lstrip # 문자열 왼쪽 공백을 제거합니다
# rstrip # 문자열 오른쪽의 공백을 제거합니다

input_a =""" 
        안녕하세요
정상수의 함수를 알아봅니다
"""
print(input_a)
print(input_a.strip())