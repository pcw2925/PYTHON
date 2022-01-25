<<<<<<< HEAD
scores = [85,71,77,90]
print(scores)

scores[1:3]
print(scores)

# 리스트 자르는법
sliced_scores =scores[1:3]
print(sliced_scores)

scores[2:4]
print(scores[0:2])
print(scores[:2])

new_scores =scores
new_scores.append(99)
print(new_scores)
print(scores)

new_scores =scores[:]
new_scores.append(100)
print(new_scores)
print(scores)

very_new_scores =new_scores.copy()
very_new_scores.append(0)
print(very_new_scores)
print(new_scores)

a= [1,2,3]
b= [4,5,6]
a +b
print(a+b)
c= a+b
print(a+b+c)

a.extend(b)
print(a)
=======
scores = [85,71,77,90]
print(scores)

scores[1:3]
print(scores)

# 리스트 자르는법
sliced_scores =scores[1:3]
print(sliced_scores)

scores[2:4]
print(scores[0:2])
print(scores[:2])

new_scores =scores
new_scores.append(99)
print(new_scores)
print(scores)

new_scores =scores[:]
new_scores.append(100)
print(new_scores)
print(scores)

very_new_scores =new_scores.copy()
very_new_scores.append(0)
print(very_new_scores)
print(new_scores)

a= [1,2,3]
b= [4,5,6]
a +b
print(a+b)
c= a+b
print(a+b+c)

a.extend(b)
print(a)
>>>>>>> c8972487c167e5b584b2368dfcbf253f25905782
