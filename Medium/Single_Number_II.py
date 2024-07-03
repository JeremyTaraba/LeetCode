class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Counter is very useful for just counting occurrences 
      
        collection = Counter(nums)

        
        return collection.most_common()[-1][0]