import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #法一：
        n1 = len(s)
        n2 = len(t)
        if n1 != n2:
            return False
        my_list = []
        for char in s:
            my_list.append(char)
        for char in t:
            if char in my_list:
                my_list.remove(char)
            else:
                return False
        return len(my_list) == 0
        
        #法二：固定数组法
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for num in count:
            if num != 0:
                return False
        return True

        #法三：
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       return collections.Counter(s) == collections.Counter(t)