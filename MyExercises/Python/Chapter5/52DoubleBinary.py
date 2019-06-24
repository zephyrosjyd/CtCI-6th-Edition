def solution(num):
    if num >= 1 or num < 0:
        return 'ERROR'
    answer = ['.']
    while num > 0:
        if len(answer) > 32:
            return 'ERROR'
        num *= 2
        print(num)
        if num >= 1:
            answer.append('1')
            num -= 1
        else:
            answer.append('0')

    return ''.join(answer)


n = 0.72
print(bin(int(n*100)))
a = solution(n)
print(a)
