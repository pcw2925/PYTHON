# number_input_a =input('숫자입력')
# radius =float(number_input_a)

# print(2*3.14 *radius)
# print(3.14 *radius *radius)

# #함수를 활용한 코드
# def number_input():
#     output =input("숫자를 입력")
#     return float(output)
# def get_cir(radius):
#     return 2*3.14 *radius
# def get_jeongsangsu(radius):
#     return 3.14 *radius *radius

# radius =number_input()
# print(get_cir(radius))
# print(get_jeongsangsu(radius))

# # 코드 유지보수
# PI =3.14
# def get_cir(radius):
#     return 2* PI *radius
# def get_sangsu(radius):
#     return PI* radius *radius


# def p(content):
#     return "<p class=' content-line'>{} </p>".format(content)
# print(p('안녕하세요'))
# print(p("간단한html 태그를 만드는 예시"))


# 알고리즘 모든경우탐색
앉힐수있는최소사람수 =2
앉힐수있는최대사람수 =10
전체사람의수 = 100
memo ={}

def 문제(남은사람수,앉힌사람수):
    key =str([남은사람수,앉힌사람수])
    if key in memo:
        return memo[key]
    if 남은사람수 < 0:
        return 0
    if 남은사람수 == 0:
        return 1
    count =0
    for i in range(앉힌사람수,앉힐수있는최대사람수+1):
        count +=문제(남은사람수 - i,i)
    memo[key] =count
    return count
print(문제(전체사람의수,앉힐수있는최소사람수))

# 앉힐수있는최소사람수 = 2
# 앉힐수있는최대사람수 = 10
# 전체사람의수 = 100
# memo = {}

# def 문제(남은사람수, 앉힌사람수) :
#     key = str([남은사람수, 앉힌사람수])
#     # 종료 조건
#     if key in memo :
#         return memo[key]
#     if 남은사람수 < 0 :
#         return 0
#     if 남은사람수 == 0 :
#         return 1
#     # 재귀 처리
#     count = 0
#     for i in range(앉힌사람수, 앉힐수있는최대사람수 + 1) :
#         count += 문제(남은사람수 - i, i)
#     # 메모화 처리
#     memo[key] = count
#     # 종료
#     return count

# print(문제(전체사람의수, 앉힐수있는최소사람수))