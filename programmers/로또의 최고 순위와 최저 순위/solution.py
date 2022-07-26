def solution(lottos, win_nums):
    hitlen = len(set(lottos) & set(win_nums))
    maxHitCnt = lottos.count(0) + hitlen
    minHitCnt = hitlen

    answer = [6 if 7 == (7 - maxHitCnt) else 7 - maxHitCnt, 6 if 7==(7-minHitCnt) else 7 - minHitCnt]
    return answer


if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    result = solution(lottos, win_nums)
    print(result)