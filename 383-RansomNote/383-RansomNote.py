class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = {}
        for i in magazine:
            if i in hashmap:
                hashmap[i]+= 1
            else:
                hashmap[i] = 1
        for i in ransomNote:
            if i not in hashmap or hashmap[i] == 0:
                return False
            hashmap[i] -= 1
        return True