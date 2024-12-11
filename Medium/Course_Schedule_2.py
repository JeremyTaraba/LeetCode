class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # find courses that have no prereqs first and add them to a queue
        # then do a bfs on this queue, adding the prereq to the queue until the queue is empty
        # check the res to see if we have added all the courses or not: len(res) = numCourses

        res = []
        queue = []
        prereqs = {}
        reversePrereqs = defaultdict(list)
        courses = defaultdict(int)
        # Might be easier to make a hashtable of all prereqs for each course

        '''
        courses  (keeps track of how many prereqs are needed for taking the class)
        {
            0: 0
            1: 1
            2: 1
            3: 2
        }
        prereqs  <-- actually don't need this, just need courses and reverse
        {
            0: []
            1: [0]
            2: [3]
            3: [1,2]
        }
        reversePrereqs
        {
            0: [1]
            1: [1,3]
            2: [3]
            3: [2]
        }

        put it all into 1 dict
        everything
        {
            0:{prereqs: [], reverse: [1], course: 0}
        }
        '''
        for i in range(numCourses):
            prereqs[i] = []
            everything[i] = {}

        for i in range(len(prerequisites)):
            prereqs[prerequisites[i][0]].append(prerequisites[i][1])
            courses[prerequisites[i][0]] += 1
            
        
        for k,v in prereqs.items():
            if v == []:
                queue.append(k)
            else:
                for value in v:
                    reversePrereqs[value].append(k)
        
        
        while queue:
            temp = queue.pop(0)
            res.append(temp)
            for value in reversePrereqs[temp]:
                courses[value] -= 1
                if courses[value] == 0:
                    queue.append(value)
              
            
        return res if len(res) == numCourses else []