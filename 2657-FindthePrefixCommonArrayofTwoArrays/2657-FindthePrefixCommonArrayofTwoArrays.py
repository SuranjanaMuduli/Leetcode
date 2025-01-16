class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = []
        count = 0
        hsA, hsB = set(),set()
        for i in range(len(A)):
            if A[i] in hsB:
                count += 1
            hsA.add(A[i])
            if B[i] in hsA:
                count += 1
            hsB.add(B[i])
        
        # Append the current count of common elements to the result
            res.append(count)
        return res
