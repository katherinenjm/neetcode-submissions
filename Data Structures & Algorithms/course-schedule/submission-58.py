class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        visit = set()
        def dfs(curr_course):
            if curr_course in visit:
                return False
            if prereq_map[curr_course] == []:
                return True

            visit.add(curr_course)
            for prereq in prereq_map[curr_course]:
                if not dfs(prereq):
                    return False
            visit.remove(curr_course)
            prereq_map[curr_course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
