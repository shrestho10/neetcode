class Solution():
    def groupAnagrams(self, strs:list[str])-> list[list[str]]:

        list_of_dicts=[]

        for i in range(len(strs)):
            list_of_dicts.append({j:0 for j in range(26)})


        for i in range(len(strs)):
            for each_char in strs[i]:
                key= ord(each_char)-ord("a")
                list_of_dicts[i][key]+=1

        checker_dict={}


        for i in range(len(strs)):
            if tuple(list_of_dicts[i].items()) not in checker_dict.keys():
                checker_dict[tuple(list_of_dicts[i].items())]=[]
                checker_dict[tuple(list_of_dicts[i].items())].append(strs[i])
            else:
                checker_dict[tuple(list_of_dicts[i].items())].append(strs[i])



        
        return list(checker_dict.values())
    


obj= Solution()
print(obj.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))






