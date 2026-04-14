class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq_map = {course: [] for course in range(numCourses)}
        seen = set()
        cycle = set()
        res = []

        for course, preq in prerequisites:
            preq_map[course].append(preq)

        def dfs(course):
            if course in cycle:
                return False
            if course in seen:
                return True

            cycle.add(course)
            for preq in preq_map[course]:
                if not dfs(preq):
                    return False

            cycle.remove(course)
            seen.add(course)
            res.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return []

        return res