# 반복문
i =1
result =0

# i가 9보다 작거나 같을때 아래 코드를 반복적으로 실행
while i <=9:
    result += i
    i +=1

print(result)

# 홀수만
i =1
result =0

# i가 9보다 작거나 같을때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i +=1
print(result)

# for 문
result =0
# i는 1부터 9까지 모든 값을 순회
for i in range(1,10):
    result +=i
print(result)

score =[90,85,11,23,56]

for i in range(5):
    if score[i] >= 80:
        print(i+1, "번 학생은 합격입니다")
        
        
scores =[90,11,55,69,91]
cheating_list ={2,4}

for i in range(5):
    if i+1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다")
        
# 2단부터 9단
for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j, "=",i*j)
    print()
