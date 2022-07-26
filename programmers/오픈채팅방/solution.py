def solution(record):
    users = {}
    body = [history.split(' ') for history in record]
    
    print(body)
    
    for history in body:
        if history[0] == 'Enter' or history[0] == 'Change':
            users[history[1]] = history[2]
            
    answer = []
    for history in body:
        content = ''
        if history[0] == 'Enter':
            content = users[history[1]] + '님이 들어왔습니다.'
            answer.append(content)
        if history[0] == 'Leave':
            content = users[history[1]] + '님이 나갔습니다.'
            answer.append(content)
        
    
    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    
    result = solution(record)
    print(result)