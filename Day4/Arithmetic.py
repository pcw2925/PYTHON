# 산술연산자

print(3+3)
print(3*4)
print(3 /6)
print(3+2+1+1)
print(20-5)



print(3 **2)  # 제곱 
print(7 /3) # 소수점까지다나옴
print (7 // 3) # 몫만나옴 

print( 7 % 3) # 나머지 

# 홀짝 구분하기
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    print(numbers)
    
if 1 % 2 == 1:
    print("홀수")
    
if 2 % 2 == 0:
    print("짝수")
    
print(numbers)
for number in numbers:
    if number % 2 == 1:
        print(number,"는홀수")
    else:
        print(number,"는짝수")