# number 내부에 들어 있는 숫자가 몇 번 등장하는지를 출력하는 코드
numbers =[1,2,3,4,5,2,3,3,1,2,3,5,7,8,9,9,1,2,3,4,6,7,8,9,0,0]
counter ={}

for number in numbers:
    if number in counter:
        counter[number] =counter[number] +1
    else:
        counter[number] = 1
print(counter)