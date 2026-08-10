class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        c1 = 0

        for num in st:
            if num - 1 not in st:
                c2 = 0
               

                while num + c2 in st:
                    c2 += 1
                    

                c1 = max(c1, c2)

        return c1
        