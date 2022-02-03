python ='python is amazing'
print(python.lower()) # 소문자출력
print(python.upper()) # 대문자로 출력
print(python[0] .isupper()) # 첫번째 문자가 대문자인지
print(len(python)) # 문자열 길이 반환
print(python.replace("python" ,'java')) # 값 변환

index = python.index('n')
print(index)


index = python.index("n", index + 1)
print(index)

print(python.find("java")) 
print(python.index("python"))

print('hi')
print(python.count("n"))