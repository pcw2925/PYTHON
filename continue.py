has_owner =''
while has_owner != '예' :
    is_space =input("우주정거장임? (예/아니요)")
    
    if is_space =="예" :
        print('다시 처음으로 돌아갑니다')
        continue # continue 를 만나면 다시 while 문으로 돌아감
    
    has_owner =input('주인이 있나요? (예/아니요)')
    
    if has_owner =='예' :
        print('처음으로 돌아갑니다')
    else :
        print("야호! 통과")
        print("주사위를 던져서 다시 실행합니다")

print('프로그램을 종료합니다')