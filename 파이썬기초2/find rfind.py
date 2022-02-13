output_a ='안녕하세요'.find("안녕")
print(output_a)

output_b ='안녕하세요'.rfind("안녕")
print(output_b)

print("안녕" in '안녕하세요')

print("정상수" in "정상수하세요")

a = "10 20 30 40 50".split(" ")
print(a)

# 조건 연산자
print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >=100)

# 문자열 비교 연산자
# 가방과 하마를 비교하면 사전순서로 가방이 앞에 있음 
print("가방" == "가방")  # 같다
print("가방" != "하마") # 같지않다
print("가방" < "하마") # 가방은 하마보다 작다
print("가방" > "하마") # 가방은 하마보다 크다 

# 범위구하기
x =25
print(10 < x < 30)

print(40 < x < 60)

# not 연산자
print(not True)
print(not False)

# not 연산자 조합하기
x =10
under_20 =x < 20
print("under_20::" ,under_20)
print("not under_20:" ,not under_20)

# and 연산자는 둘다 참이여야 True
# or 연산자는 하나만 참이여도 True


