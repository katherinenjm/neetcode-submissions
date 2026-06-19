class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        anag_hashm = {}
        for word in strs:
            charact_tracker = [0] * 26
            for charact in word:
                charact_tracker[ord(charact)- ord('a')] += 1
            if tuple(charact_tracker) not in anag_hashm:
                anag_hashm[tuple(charact_tracker)] = []

            anag_hashm[tuple(charact_tracker)].append(word)
        return list(anag_hashm.values())


                
        # #implement bucket sort for elem in str
        # #maybe start off with just sort and go from there
        # #append values into hashmap with elem.sorted = key, append index
        # # print('a'<'c')

        # # def bucketSort(str,len(arr)):
        # if not strs:
        #     return [[]]


        # sorted_word_hashm = {}
        # for i in range(len(strs)):
        #     word = ''.join(sorted(strs[i]))
        #     if word not in sorted_word_hashm:
        #         sorted_word_hashm[word] = []
        #     sorted_word_hashm[word].append(strs[i])
        
        # return(list(sorted_word_hashm.values()))
        

        # #empty list
        # # for key in hashm, reate empty sublist and populate with strs[hashm[key]] for val in hashm[key]
        # #append substr to str
        
        