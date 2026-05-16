class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            
        visit_state = [0] * numCourses
        
        def has_cycle(course):
    
            if visit_state[course] == 1:
                return True
          
            if visit_state[course] == 2:
                return False
                
            visit_state[course] = 1
            
            for next_course in adj_list[course]:
                if has_cycle(next_course):
                    return True
                    
            visit_state[course] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
                
        return True