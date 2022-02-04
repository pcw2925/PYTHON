cabinet ={3: "정상수",100:"백발백중" ,6:'최종명'}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(5))
# print(cabinet.get(5,"사용가능"))
# print('hi')

# # print(cabinet[5])
# # print('hi')

print(3 in cabinet)  #True
print(5 in cabinet)  #False
print(6 in cabinet)  #True


cabinet ={"A-3": "정상수",'B-199':"백발백중" ,6:'최종명'}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "박철만"
cabinet["C-20"] ='최한석'
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)


# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)