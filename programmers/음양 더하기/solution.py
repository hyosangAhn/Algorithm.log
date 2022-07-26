def solution(absolutes, signs):
    for i, sign in enumerate(signs):
        if not sign:
            absolutes[i] = -absolutes[i]

    answer = sum(absolutes)
    return answer


if __name__ == '__main__':
    absolutes = [4,7,12]
    signs = [True, False, True]
    
    result = solution(absolutes, signs)
    print(result)