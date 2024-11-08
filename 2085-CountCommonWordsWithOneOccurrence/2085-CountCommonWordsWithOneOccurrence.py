class Solution(object):
    from collections import Counter
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        hm1 = Counter(words1)
        hm2 = Counter(words2)
        
        uni_words1 = {word for word, count in hm1.items() if count == 1}
        uni_words2 = {word for word, count in hm2.items() if count == 1}
        
        common_unique_words = uni_words1 & uni_words2
        
        # Step 4: Return the count of such words
        return len(common_unique_words)
            