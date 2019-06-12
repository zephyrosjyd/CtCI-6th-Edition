# O(N)
import unittest


def string_compression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)


def compression(string):
    from collections import Counter
    counter = Counter(string)
    if len(counter) *2 >= len(string):
        return string
    result = [k + str(counter[k]) for k in counter]
    return ''.join(result)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

    def test_string_compression2(self):
        for [test_string, expected] in self.data:
            actual = compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
