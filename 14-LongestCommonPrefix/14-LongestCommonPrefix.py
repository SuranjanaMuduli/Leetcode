class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
    
        # Find the shortest string in the list
        shortest = min(strs, key=len)
        
        # Compare each character in the shortest string with others
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        
        return shortest

    # class Solution:
    #     def longestCommonPrefix(self, m):
    #         if not m: return ''
    #     			#since list of string will be sorted and retrieved min max by alphebetic order
    #         s1 = min(m)
    #         s2 = max(m)

    #         for i, c in enumerate(s1):
    #             if c != s2[i]:
    #                 return s1[:i] #stop until hit the split index
    #         return s1