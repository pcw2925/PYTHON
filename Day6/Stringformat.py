print('a' +'b')
print("a","b")

# 방법 1
print('나는 %d살입니다' % 20) # 정수
print('나는 %s 를 좋아해요' % "파이썬") # %s 문자열 스트링값
print("Apple 은 %c로 시작해요." % "A") # 문자 

print('나는 %s살입니다' % 20) # 정수
print('나는 %s 색과 %s 색을 좋아해요' % ('파란색','빨간색'))

# 방법 2
print("나는 {} 살입니다." .format(200))
print("나는 {} 색과 {} 색을 좋아해요" .format('파란','빨간'))

print("나는 {0} 색과 {1} 색을 좋아해요" .format('파란','빨간'))
print("나는 {1} 색과 {0} 색을 좋아해요" .format('파란','빨간'))

# 방법 3
print("나는 {age} 살이며 ,{color} 정상수를 좋아해요.".format(age =20 ,color="빨간"))
print("나는 {color} 살이며 ,{age} 정상수를 좋아해요.".format(age =20 ,color="빨간"))

# 방법 4
age = 20
color ='빨간'
print(f"나는 {age} 살이며 ,{color} 정상수를 좋아해요.")