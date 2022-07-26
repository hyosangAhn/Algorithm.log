import math
import itertools

def solution(nums):
    cnt = 0
    for iter in itertools.combinations(nums, 3):
        cnt += 0 if is_prime(sum(iter)) else 1
    return cnt

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


if __name__ == '__main__':
    nums = [1,2,3,4]

    result = solution(nums)
    print(result)