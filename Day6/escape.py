# 탈출문자
from re import M


print('백발백중하는\n빡빡이 정상수')

print("저는 정상수입니다")
print('저는 "정상수"입니다.')

print('저는 \"정상수"입니다')

# \ \ : 문장 내에서 \ 로 바뀜
print("C:\\Users\\박찬우\\Python\\Python>") # 경로출력

#  \r  : 커서를 맨 앞으로 이동해준다
print('Red Apple\rpine')

#  \b : 백스페이스 ( 한글자 지움)
print("Redd\bApple")

# \t 탭 역할을함
print('Red\tApple')

# quiz
# 사이트별로 비밀번호를 만들어주는 프로그램을 작성
# 예 http://naver.com

url ='http://youtube.com'
my_str = url.replace("http://" ,"") 
print(my_str)

my_str =my_str[:my_str.index(".")] # my_str[0:5] 0 부터 5직전까지

print(my_str)


password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) +"1"
print("{0} 의 비밀번호은{1} 입니다.".format(url,password))