
class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        d= 1 << k
        l= set()
        num=0
        for i in range(len(s)):
            num=((num << 1)&(1 << k)-1 | int(s[i]))
            if i>=k-1:
                l.add(num)
                if len(l)==d:
                    return True
        return False