import random
ans1 =" check this out 나는 정상수"
ans2 ="백발백중하는명사수"
ans3 ="부산진구 유명가수"
ans4 ="내가대표해 이거리를"
ans5= "누구도막지못해 내짓거림을"
ans6= "사양할게 난 너의 피쳐링을"
ans7 ="계속해서 매섭게 쏘겟어"
ans8= "반말하지마세요"


print("my정상수 게임에 오신걸 환영합니다.")
question =input("조언을 구하고 싶으면 질문을 입력하고 엔터키를 눌러라\n")

print("고민중 ...\n" *4)

choice=random.randint(1,8)
if choice==1:
    answer=ans1
elif choice ==2:
    answer=ans2
elif choice ==2:
    answer=ans2
elif choice ==3:
    answer=ans3
elif choice ==4:
    answer=ans4
elif choice ==5:
    answer=ans5
elif choice ==6:
    answer=ans6
else:
    answer=ans8
    
print(answer)
input("\n\n 마치려면 엔터키를 누르십시요")