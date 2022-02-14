character = {
    'name':'정상수',
    "level":'13',
    "items":{
        "sword": "상수의검",
        "armor": "백발백중하는 명사수"
    },
    "skill" :["베기",'정상수베기','정상수탈모']
    }
for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key,":",character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key,":",item)
        else:
            print(key,":",character[key])
