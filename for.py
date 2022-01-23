has_owner =''
while has_owner != '예' :
    has_owner =input("주인이 있나요? (예/아니요)")
    
    if has_owner =='예' :
        print('통행료를 지불하세요!')
    else :
        print("야호! 통과")
        print("주사위를 던져서 다시 실행합니다")

print('프로그램을 종료합니다')