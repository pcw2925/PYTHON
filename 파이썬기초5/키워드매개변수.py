def function(일반매개변수A,일반매개변수B,*가변매개변수,기본매개변수A=10,기본매개변수B=20):
    print(일반매개변수A,일반매개변수B)
    print(가변매개변수)
    print(기본매개변수A, 기본매개변수B)
    
print(""",""",end=' ')
function(0,1,2,3,4,5,6,7,8,9,10,기본매개변수A=11,기본매개변수B=12)
# 순서 상관없음

print(1,2,3,4,sep="| |")

# 여러함수 호출형태
def test(a, b=10, c=100):
    print(a+b+c)
    
test(10,20,30)
test(a=10, b=100,c=200)
test(c=10, a=100,b=200)
test(10, c=200)

# 자료없이 리턴하기
def function():
    print("A")
    print("b")
    return  # 값을들고 돌어감  함수의결과 =리턴된값 
    print("C")
    print("D")
    
print(function())


# 함수
# start-end  까지 있는 모든 정수를 더하는 함수
def sum_all(start,end):
    변수  = 0
    # 100에다가 0 더해도 0
    for i in range(start,end +1):
        변수 += i 
    return 변수
    
print(sum_all(1,1000))
print(sum_all(50,100))

# 방정식 함수로 만들기
def f(x):
    return (2*x) +1
print(f(10))

def f_2(x):
    return (x**2)+(2 *x) +1
print(f_2(10))

# 가변매개변수 함수 만들기
def mul(*values):
    변수 =1
    for i in values:
        변수 *= i
    return 변수

print(mul(5,7,9,10))