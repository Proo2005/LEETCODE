class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()

        def insert(num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        def getMax(num):
            node = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit
                if toggled in node.children:
                    xor |= (1 << i)
                    node = node.children[toggled]
                else:
                    node = node.children[bit]
            return xor

        for num in nums:
            insert(num)

        ans = 0
        for num in nums:
            ans = max(ans, getMax(num))

        return ans