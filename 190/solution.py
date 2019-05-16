class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:]
        b = '0' * (32 - len(b)) + b
        return int("".join(list(reversed(list(b)))), 2)
