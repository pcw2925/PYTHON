key_list = ["name","hp","mp","level"]
value_list =["기사",'200','30','5']
character ={}

for i in range(0,len(key_list)):
    character[key_list[i]] =value_list[i]
print(character)

# 1부터 숫자를 더하는 경우
limit =10000
i =1

sum_value =0
while sum_value < limit:
    sum_value += i
    i +=1
print("{} 더할때 {} 을 넘으며 그때의 값은{}입니다 \n".format(i,limit,sum_value))


# 1부터 100까지 숫자 최대가 되는 경우
max_value =0
a =0
b =0

for i in range(1,100 // 2 + 1):
    j =100 -i
    
    current =i * j
    if max_value <current:
        a = i
        b =j
        max_value =current
print("{} 최대가 되는 경우 {} *{}".format(a,b,max_value))