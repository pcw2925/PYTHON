# 기둥과 보설치
def possible(answer):
    for x,y,stuff in answer:
        if stuff == 0: # 설치된 것이 기둥인 경우
            if y == 0 or [x-1,y,1] in answer or[x,y,1] in answer or[x,y -1,0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y -1,0] in answer or [x+1,y-1,0] in answer or([x-1,y,1] in answer and[x+1,y,1] in answer):
                continue
            return False
        return True

def solution(n,bulid_frame): 
    answer =[]
    for frame in bulid_frame:
        x,y,stuff,operate =frame # 작업의 개수는 최대 1000개
    if operate == 0: # 삭제하는경우
        answer.remove([x, y,stuff]) # 일단 삭제를 해본 뒤에
        if not possible(answer): # 가능한 구조물인지 확인
            answer.append([x,y,stuff]) # 가능한 구조물이 아니라면 다시 설치
    if operate == 1:
        answer.append([x,y,stuff]) # 일단 설치를 해본 뒤에
        if not possible(answer): # 가능한 구조물인지 확인
            answer.remove([x,y,stuff]) # 가능한 궂물이 아니라면 다시 제거
        return sorted(answer) # 정렬된 결과를 반환
    
                                                                
