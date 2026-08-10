class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        answer = []
        i = 0
        num = 1
        for i in range(len(nums)):
            num = num * nums[i]
            prefix.append(num)
        num = 1
        for i in range(len(nums)-1 , -1 ,-1):
            num = num * nums[i]
            postfix.append(num)
        num = 1
        postfix.reverse()

        for i in range(len(nums)):
            if i == 0:
                num = postfix[i+1]
                answer.append(num)
                num = 1
            elif i == (len(nums)-1):
                num = prefix[i-1]
                answer.append(num)
                num = 1
            else:
                num = prefix[i-1] * postfix[i+1]
                answer.append(num)
                num = 1
        return answer
            