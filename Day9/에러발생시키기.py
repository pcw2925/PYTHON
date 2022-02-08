# 의도적으로 에러를 발생
try:
    print("한자리 숫자 나누기 전용 계산기 입니다")
    num1 =int(input("첫번째 숫자를 입력하세요 :"))
    num2 =int(input('두 번째 숫자를 입력하세요 :'))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} /{1} ={2}".format(num1,num2,int(num1 /num2)))
except ValueError:
    print('잘못된 값을 입력하엿습니다. 한자리 숫자를 입력하세요')


