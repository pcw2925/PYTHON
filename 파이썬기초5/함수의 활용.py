# 재귀함수와 메모화
# 팩토리얼
def factorial_1(n):
    변수 =1
    for i in range(1,n +1):
        변수 *= i
    return 변수

# 두번째 방법
# n! n* (n-1)
# 0! =1
def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n *factorial_2(n-1)
print(factorial_1(3))
print(factorial_2(3))

# 재귀 함수의 문제
counter =0
def f(n):
    global counter
    counter +=1
    if n == 1 or n ==2:
        return 1
    else:
        return f(n-1) +f(n-2)
print(f(20))
print(counter)

# 메모화
메모 = {1:1,2:1}
def f(n):
# 변수선언 
 if n in 메모:
   return 메모[n]
 else:
    output = f(n-1) +f(n-2)
    메모[n] =output
    return output
print(f(200))

# 조기리턴 = 이후 함수 실행을 차단하는 기술 
 