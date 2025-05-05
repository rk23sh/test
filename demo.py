import math
class Solution:
    def closestPrimes(self, left: int, right: int):
        def sieve(n):
            l = [1 for i in range(n+1)]
            l[0] = 0
            l[1] = 0
            for i in range(2, n+1):
                if l[i]==0: continue
                for j in range(i*i, n+1, i): l[j] = 0
            print(l)
            prime_list = [ idx for idx, value in enumerate(l) if value==1 ]
            return prime_list
        
        prime_list = sieve(int(math.sqrt(right))+1)

        def segmented_sieve(prime_list):
            print(prime_list)
            dummy_array = [ 1 for i in range(right-left+1) ]
            for i in prime_list:
                low = math.ceil(left//i)
                low = max(low, i)
                for j in range(low*i, right+1, i): dummy_array[j-left] = 0
            
            final_array = [ left+idx for idx, value in enumerate(dummy_array) if value==1 ]
            return final_array
        
        final_array = segmented_sieve(prime_list)

        return final_array
    

s = Solution()
print(s.closestPrimes(10, 19))



