for i in range(100):
    print("정상수")
    
# for 반복문과 리스트
# 리스트를 선언합니다
array =[273,32,103,56,23]

for element in array:
    print(element)
    
numbers =[273,103,5,322,65,9,72,800,99]
# 홀수 짝수 자릿수 프로그램 
for number in numbers:
    print(number,"는",len(str(number)),"자릿수입니다.")

# 숫자를 하나하나 출력하는 프로그램 
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for line in list_of_list:
    for item in line:
        print(item)
        
numbers =[1,2,3,4,5,6,7,8,9]
output =[[],[],[]]

for number in numbers:
    output[(number +2) %3].append(number)
    print(output)
