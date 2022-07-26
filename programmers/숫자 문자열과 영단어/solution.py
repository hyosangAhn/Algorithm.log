def solution(s):
    numDic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for key, value in numDic.items():
        s = s.replace(key, str(value))
        
    answer = s
    return int(answer)

if __name__ == '__main__':
    s = "one4seveneight"
    
    result = solution(s)
    print(result)