# 슬라이싱
jumin ="123457-1752212"

print('성별 :' +jumin[7])
print('년도 :' +jumin[0:2]) # 0부터 2직전까지
print("월 :" +jumin[2:4])
print('일 :' +jumin[4:6])

print("생년월일:" +jumin[0:6])
print("뒷자리: "+ jumin[7:14])

print("뒤 7자리 (뒤에서부터): "+ jumin[-7:])
# 맨뒤에서 7번째 부터 끝까지 