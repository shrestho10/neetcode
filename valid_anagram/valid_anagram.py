class Solution:
    def validAnagram(self,s:str,t:str)-> bool:
        source_dict={i:0 for i in range(26)}
        target_dict={i:0 for i in range(26)}

        for i in s:
            key = ord(i)-ord("a")
            source_dict[key]+=1
        

        for i in t:
            key = ord(i)-ord("a")
            target_dict[key]+=1

        if source_dict==target_dict:
            return True
        else:
            return False
        



obj = Solution()
print(obj.validAnagram("jar", "jam"))      # False
print(obj.validAnagram("listen", "silent"))  # True
print(obj.validAnagram("racecar", "carrace")) # True
print(obj.validAnagram("rat", "car"))      # False






 