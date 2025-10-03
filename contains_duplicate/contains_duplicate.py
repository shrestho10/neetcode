class Solution:
    def hasDuplicate(self, nums:list[int]) -> bool:
        checker_dict={}
        for i in nums:
            if i not in checker_dict.keys():
                checker_dict[i]=1
            else:
                return True
            
        return False
    

obj=Solution()
print(obj.hasDuplicate([1,2,3,4,0,4]))