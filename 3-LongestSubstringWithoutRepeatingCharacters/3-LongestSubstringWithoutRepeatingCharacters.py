class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        hashset = set()
        i,j =0,0
        while j<len(s):
            if s[j] not in hashset:
                hashset.add(s[j])
                j +=1
                ans = max(ans,len(hashset))
            else:
                hashset.remove(s[i])
                i +=1
        return ans