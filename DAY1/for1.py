# for word in '재밌는 파이썬 프로그래밍' :
#     print(word)
 # range 는 0부터 시작 
for n in range(1,101) :
    print(n,"번 실행")
    

for n in range(1,11,2):
    print("check this out 나는 정상수")
    # 마지막 증가되는 폭
    
for n in range(1,11):
    if n % 2 == 0 :
            continue
    print(n,"번 실행")
    
for n in range(1,11):
    if n == 5 :
            break
    print(n,"번 실행")
    