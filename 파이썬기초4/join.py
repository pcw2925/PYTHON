# join 함수 리스트의 요소를 문자열로 연결함 
print("::".join(['1','2','3','4','5']))

number =int(input("정상수입력"))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {} 입니다.\n"
        "{}는 짝수 입니다."
    ]).format(number,number))
else:
       print("\n".join([
        "입력한 문자열은 {} 입니다.\n"
        "{}는 홀수 입니다."
    ]).format(number,number))
       
# reversed() 함수와 이터레이터
numbers =[1,2,3,4,5,6]
r_num =reversed(numbers)

# reversed_numbers를 출력합니다
print('reversed_numbers:',r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# 1부터 100까지 사이 숫자중 2진수 변환 0이 하나만 포함된 숫자를 찾고
# 숫자들의 합을 구하는 코드 작성하기
output = [i for i in range(1,100 +1)
         if "{:b}".format(i).count("0") ==1]

for i in output:
    print('{} : {}'.format(i,"{:b}").format(i))
print("합계:" ,sum(output)) 