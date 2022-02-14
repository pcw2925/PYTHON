정상수 = {
    "name" : "정상수게임",
    "type" : "정상수무비"
}
print(정상수)

dict_b ={
    "director":["안소니 루소",'조 루소'],
    "cast": ["아이언맨",'타노스','토르','닥터스트레인지','헐크']
    
}
print(dict_b)


dictionary = {
    "name": "7D 건조 망고",
    'type': "당절임",
    "ingredient": ["망고",'설탕','메타중아황산나트륨','치자황색소'],
    "origin" :"필리핀"
}

print("name:",dictionary["name"])
print("type:" ,dictionary["type"])
print("ingredient:",dictionary["ingredient"])
print("origin:" ,dictionary["origin"])
print()

# 값을 변경
dictionary["name"] ="8D 건조 망고"
print("name:", dictionary["name"])

name ="이름"
dict_key ={
    name: "정상수",
    type: "백발백중"
}
print(dict_key)

# price값 5000 추가
dictionary["price"] =5000
print(dictionary)

dictionary["name"]= '백발백중하는 명사수'
print(dictionary)

del dictionary["ingredient"]
print(dictionary)

# 딕셔너리 요소에 추가하기
dictionary1 ={}

print("요소 추가이전:",dictionary1)

dictionary1["name"] ='정상수'
dictionary1["head"] ="백발백중 정신"
dictionary1["body"] = "정상수 몸"
print("요소 추가 이후:",dictionary1)