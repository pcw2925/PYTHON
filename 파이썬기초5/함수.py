# 함수를 선언헌다
def 함수이름(매개변수1,매개변수2,매개변수3,매개변수4):
    print("백발백중 하는 명사수" +str(매개변수1))
    print("백발백중 하는 명사수" +str(매개변수2))
    return 매개변수1 +매개변수2+ 매개변수3+ 매개변수4
    print("백발백중 하는 명사수" +str(매개변수3))
    print("백발백중 하는 명사수" +str(매개변수4))
    
     # 실행되지않음
    
# 함수를 호출한다
print(함수이름(100,200,300,400)) # 매개변수 1 2 3 4에 값이 들어감 


# # 함수 복습
# def print_n_times(value,n):
#     for i in range(n):
#         print(value)

# # print_n_times("백발백중하는명사수1") # 지정한 
# # 매개변수보다 적으면 오류발생
# print_n_times("백발백중하는 명사수",5) 


print("정상수1")
print("정상수 육변기",2)
print("백발백중하는 명사수",4,100)


# 가변 매개변수 함수
# 함수에서 하나만 사용 가능함 
# 가변 매개변수 마지막위치에 올수있음 * 가변매개변수 표시
def 함수이름(정상수1,정상수2, *가변정상수):
    print(정상수1)
    print(정상수2)
    print(가변정상수)
    
함수이름(0,1,2,3,4,5,6,7,8,9)


# 기본 매개변수
def print_n_times(value,n=200): # 매개변수 위치를 바꾸면안됨
    for i in range(n):
        print(value)
        
print_n_times("백발백중하는 명사수") # 기본매개변수 마지막에입력

def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(2000,'안녕하세요','즐거운','정상수프로그래밍')


