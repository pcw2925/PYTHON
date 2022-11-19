import sys
input = sys.stdin.readline

# 노드수 n, 여행계획 수 m
n,m = map(int, input().split())

parent = [0] *(n+1)
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            union_parent(parent,i,j)

plan = list(map(int, input().split()))

result = False

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent,plan[i-1]):
        result = True
        break

if result == True:
    print("NO")
else :
    print("YES")