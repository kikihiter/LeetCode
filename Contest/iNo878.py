#必然的超时超界，没来得及想后续
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        i,k = 1,0
        while k < N and i <10**9+8:
            if i%A == 0 or i%B == 0:
                k += 1
                ans = i
            if i == 10**9+8:
                ans = i
            i += 1
        return ans
