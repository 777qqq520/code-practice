class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0,1)      #一直不return，说明所有位都是9，进位后变为1000...0，所以在首位插入1
        return digits 