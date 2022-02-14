dictionary ={
        "name": '정상수',
        'type':'백발백중'
}
print("요소 제거 이전:",dictionary)

# 제거
del dictionary["name"]
del dictionary["type"]

print("요소 제거이후:",dictionary)

dictionary ={
    "name": "7D건조 망고",
    "type": "당절임",
    "ingredient" :["망고",'설탕','메타중아황산나트륨','치자황색소'],
    "origin":"필리핀"
}

key =input("접근하고자 하는키: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는키에 접근하고있습니다")


# 키가 존재하지 않을때 None을 출력하는지 확인하기
dictionary ={
    "name": '7D 건조망고',
    "type": '당절임',
    "ingredinet":["망고",'설탕','정상수','백발백중'],
    "origin": "대한민국"   
}

value =dictionary.get("존재하지 않는 키")
print("값",value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
    
# for 반복문과 딕셔너리
dictionary ={
    "name": '7D 건조망고',
    "type": '당절임',
    "ingredinet":["망고",'설탕','정상수','백발백중'],
    "origin": "대한민국"   
}
for key in dictionary:
    print(key,":",dictionary[key])