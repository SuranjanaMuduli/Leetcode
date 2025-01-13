from collections import Counter
class Solution(object):
    def minimumLength(self, s):
        mp = Counter(s)
        ans = 0
        for ch, cnt in mp.items():
            ans += 1
            if not cnt % 2:
                ans += 1
        return ans