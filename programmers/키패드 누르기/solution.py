def solution(numbers, hand):
    answer = ""
    left = 10
    right = 12

    for num in numbers:
        if num == 0:
            num = 11
        if num % 3 == 0:
            answer += "R"
            right = num
        elif num % 3 == 1:
            answer += "L"
            left = num
        else:
            ml = abs(left - num) #4-5 = 1
            mr = abs(right - num)  #
            dl = ml // 3 + ml % 3
            dr = mr // 3 + mr % 3
            if dl > dr:
                answer += "R"
                right = num
            elif dl < dr:
                answer += "L"
                left = num
            else:
                if hand == "right":
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num

    return answer


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    
    result = solution(numbers, hand)
    print(result)