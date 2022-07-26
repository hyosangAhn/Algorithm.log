def solution(numbers):
    nums = [i for i in range(10)]
    return sum(set(nums) - set(numbers))

if __name__ == '__main__':
    numbers = [1,2,3,4,6,7,8,0]
    
    result = solution(numbers)
    print(result)