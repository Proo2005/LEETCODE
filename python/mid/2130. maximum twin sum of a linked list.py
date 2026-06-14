class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []

        current = head
        while current:
            a.append(current.val)
            current = current.next

        ans = 0
        n = len(a)

        for i in range(n // 2):
            ans = max(ans, a[i] + a[n - 1 - i])

        return ans