def insert_bits(n, m, i, j):
    answer = n & (-1 << j)
    print(bin(answer))
    answer += m << i
    print(bin(answer))
    answer += n & ~(-1 << i)
    return answer

def insert_bits2(n, m, i, j):
    return (n & (-1 << j)) | (m << i) | (n & ~(-1 << i))

n = 0b101100110101
print(bin(n))
m = 0b10101
print(bin(m))
a = insert_bits2(n, m, 3, 7)
print(bin(a))
