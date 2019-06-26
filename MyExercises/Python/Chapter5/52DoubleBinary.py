def solution(num):
    if num >= 1 or num < 0:
        return 'ERROR'
    answer = ['.']
    while num > 0:
        if len(answer) > 32:
            return 'ERROR'
        r = num * 2
        # print(num, r)
        if r >= 1:
            answer.append('1')
            num = r - 1
        else:
            answer.append('0')
            num = r

    return ''.join(answer)

def solution2(num):
    if num >= 1 or num < 0:
        return 'ERROR'
        
    import math
    answer = ['.']
    n = 1
    while n <= 32 and num > 0:
        if num >= math.pow(2, -n):
            num -= math.pow(2, -n)
            answer.append('1')
        else:
            answer.append('0')
        n += 1
    
    if n > 32 and num > 0:
        return 'ERROR'
    return ''.join(answer)


n = 0.625
# print(bin(int(n*100)))

print(solution(0.625), solution2(0.625))
print(solution(0.312), solution2(0.312))
print(solution(0.6), solution2(0.6))
