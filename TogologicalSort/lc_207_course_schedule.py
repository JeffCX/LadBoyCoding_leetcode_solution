# Python 3.7.0

from queue import Queue

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        """
            Time Complexity: O(n + v), n is number of dependency, v is number of courses
        """
        
        # create graph
        graph_dic = {}
        course_lst = [0] * numCourses
        
        for course, prerequiste in prerequisites:
            if prerequiste not in graph_dic:
                graph_dic[prerequiste] = [course]
            else:
                graph_dic[prerequiste].append(course)
            course_lst[course] += 1
            
        # put courses that have no prerequite into the queue
        q = Queue()
        for course in range(len(course_lst)):
            if course_lst[course] == 0:
                q.put(course)
        
        # topological sort
        while not q.empty():
            
            course = q.get()
            if course in graph_dic:
                for next_course in graph_dic[course]:
                    course_lst[next_course] -= 1
                    if course_lst[next_course] == 0:
                        q.put(next_course)
        
        # check if we can complete all courses
        for course in course_lst:
            if course > 0:
                return False
        
        return True
        