import math

def solution(s):
    # print(len(s)) #문자열 개수
    # print(math.ceil(len(s)/2)) #최대 자를수 있는 문자열수
    result = [] 
    
    for i in range(1, math.ceil(len(s)/2)+1):
        texts = [s[j:j+i] for j in range(0, len(s), i)]
        
        cnt = 0
        combine_txt = ''
        for k in range(len(texts)):
            if k == len(texts)-1:
                if cnt > 0:
                    cnt += 1
                    combine_txt += str(cnt) + texts[k]
                    cnt = 0
                else:
                    combine_txt += texts[k]
                
                break
            
            if texts[k] == texts[k+1]:
                cnt += 1
            else:
                if cnt > 0:
                    cnt += 1
                    combine_txt += str(cnt) + texts[k]
                    cnt = 0
                else:
                    combine_txt += texts[k]
        
        result.append(len(combine_txt))
                    
        
    return min(result)


if __name__ == '__main__':
    s = "aabbaccc"

    result = solution(s)
    print(result)