class Solution:
    def topkFrequent(self,nums:list[int],k:int)->list[int]:
        
        counter_dict={}
        for i in nums:
            if i not in counter_dict.keys():
                counter_dict[i]=1
            else:
                counter_dict[i]+=1



        new_dict={}

        for i,j in counter_dict.items():
            if j not in new_dict.keys():
                new_dict[j]=[]
                new_dict[j].append(i)
            else:
                new_dict[j].append(i)
                
                
        
        final_ans=[]

        for i in range(len(nums),0,-1):
            if i in new_dict.keys():
                for j in new_dict[i]:
                    final_ans.append(j)
                    if len(final_ans)==k:
                        return final_ans
            else:
                continue


        return final_ans







obj=Solution()
print(obj.topkFrequent(nums = [1,2,2,3,3,3], k = 2))
print(obj.topkFrequent(nums = [7,7], k = 1))
            

        




        
