class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        output = []
        for i in nums:
            if i not in numbers:
                numbers[i] = 1
            else:
                numbers[i] += 1
        sortd = sorted(numbers, key = numbers.get, reverse=True)
        for j in range(k):
            output.append(sortd[j])  
        return output  


        