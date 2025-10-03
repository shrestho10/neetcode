class Solution:
    def twoSum(self, s:list[int],t=int)-> list[int]:
        checker_dict={}
        for i in range(len(s)):
            key = t-s[i]
            if key not in checker_dict:
                checker_dict[s[i]]=i
            else:
                return [checker_dict[key],i]
            

obj=Solution()
print(obj.twoSum(s = [4,5,6], t = 10))