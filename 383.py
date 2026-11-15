class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        count = [0] * 26
        for i in range(len(ransomNote)):
            count[ord(ransomNote[i])-ord('a')] += 1
        for j in range(len(magazine)):
            count[ord(magazine[j])-ord('a')] -= 1
        for num in count:
            if num > 0:
                return False
        return True