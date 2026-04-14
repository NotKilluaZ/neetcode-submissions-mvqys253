class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if pre_map[course] == []:
                return True

            seen.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            seen.remove(course)
            pre_map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True