# 딕셔너리
programers = {'python': 14,'Ruby':5,'c++':10}
print(programers)


print(len(programers))

programers['python'] =10
print(programers)

programers.keys()
print(programers)

list(programers.values())

print('python' in programers)
print('c++' in programers)

programers['Ruby']
print(programers)

del programers['Ruby']
print(programers)


programers_list =[('python',10),('Ruby',5),('c++',10)]
print(programers_list)

print(dict(programers_list))


nums =4,2,5,7,1,3

# 정렬 된 값을 반환함 
print(sorted(nums))

print(nums)


print(sorted(nums, reverse=True))

print(programers)

print(sorted(programers,reverse=True))