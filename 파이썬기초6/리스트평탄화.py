def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)                    # 자기 자신 실행(아이템 = 리스트 전달)
        else:
            ##output.append(item) 으로 해도 되고
            output += [item]
    return output
 
example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본:", example)
print("변환:", flatten(example))