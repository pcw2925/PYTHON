from collections import deque
import re

queqe= deque()

queqe.append(5)
queqe.append(2)
queqe.append(3)
queqe.append(7)
queqe.popleft() # 삭제
queqe.append(1)
queqe.append(4)
queqe.popleft() # 삭제

print(queqe)
queqe.reverse()
print(queqe)
