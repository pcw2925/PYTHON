score_file =open("score.txt","w",encoding="utf8")
print("\n백발백중:0", file =score_file)
print("영어:50", file=score_file)
score_file.close()

# ------------------------------------------------
score_file =open("score.txt" ,"a" ,encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n정상수 : 100")
score_file.close()

 #-----------------------------------------
score_file =open('score.txt' ,"r",encoding="utf8")
print(score_file.read())
score_file.close()

# -----------------------------------------
score_file =open('score.txt' ,"r",encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기 동작 수행 한줄읽고 커서 다음줄 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

 #--------------------------------------------------
score_file =open('score.txt' ,"r",encoding="utf8")
while True: # 무한루프
    line =score_file.readline()
    if not line:
        break
    print(line,end ="")
score_file.close()

# ----------------------------------------

score_file =open('score.txt' ,"r",encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line,end="")
    
score_file.close()