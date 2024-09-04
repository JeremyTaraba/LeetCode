class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # move robot according to the rules
        # check if hitting an obstacles while moving
        # make sure to record max distance 
        x,y = 0,0
        direct = [[0,1], [1,0], [0,-1], [-1, 0]]
        direction = 0 # 0 = north, 1 = east, 2 = south, 3 = west
        maxDist = 0
        setObstacles = {tuple(o) for o in obstacles}


        for num in commands:
            if num == -1:
                direction = (direction + 1) % 4
               
            elif num == -2:
                direction = (direction - 1) % 4
                
            else:
                # move forward based on direction
                dx, dy = direct[direction]
                for i in range(num):
                    if (x + dx, y + dy) in setObstacles:
                        break
                    x,y = x + dx, y + dy

                maxDist = max(x*x + y*y, maxDist)

                    
        return maxDist


        