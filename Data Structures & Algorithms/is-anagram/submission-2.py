class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashm = {}
        t_hashm = {}

        for letter_s in s:
            if letter_s in s_hashm:
                s_hashm[letter_s] += 1
            else:
                s_hashm[letter_s] = 1
        
        for letter_t in t:
            if letter_t not in s_hashm:
                return False
            else:
                if s_hashm[letter_t] != 1:
                    s_hashm[letter_t] -= 1
                else:
                    del s_hashm[letter_t]
        
        return s_hashm == {}
        
        
        