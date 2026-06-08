class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #create hashsmap with numbers of students willing to eat eat type of sammidge
        cntr = Counter(students)
        uneaten = len(students)
        for s in sandwiches:
            if cntr[s] >0:
                uneaten -= 1
                cntr[s] -= 1
            else:
                break
        return uneaten

        