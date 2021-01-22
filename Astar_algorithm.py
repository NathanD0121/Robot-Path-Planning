import sys
import math
from pprint import pprint
map = [
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
     [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]



class Map:
    def __init__(self):
        self.map = [0]
        self.initialState = [0, 0]
        self.goalState = [0, 0]

    def getMap(self, map):
        self.map = map

    def GoalState(self, goalState):
        self.goalState = goalState

    def robotState(self, initialState):
        self.initialState = initialState

    def checkGoal(self, state):
        return state[0] == self.goalState[0] and state[1] == self.goalState[1]

    def pickAlgorithm(self, algorithm):
        answer = None
        print("Robot positon: ", self.initialState)
        print("Goal position: ", self.goalState)
        if algorithm == 'astar':
            answer = self._astar()
        elif algorithm == 'heuristic':
            answer = self.heuristic()
        else:
            print("Please choose an algorithm to find the path")
            pass
        return answer

    def distance(state1, state2): #distance methots to calculate between robot pose and goal pose
        return abs(state1[0] - state2[0]) + abs(state1[1] - state2[1])  #  Manhattan Distance = |x 1 - x 2 | + |y 1 - y 2 |
        #return math.sqrt((state1[0] - state2[0]) ** 2 + (state1[1] - state2[1]) ** 2)  # Euclidian Distance = square root((x 1 - x 2)^2 + (y 1 - y 2) ^2 )

    def printPath(self, answer): #to see the path on array map as an output.
        path = []
        path[:] = self.map
        for idx, step in enumerate(answer):
            y = step[0]
            x = step[1]
            path[y][x] = idx
        return path

    def findEmptyCells(self, state):
        lrdu = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # look left,right,down,up
        leny = len(self.map)
        lenx = len(self.map[0])
        emptyCells = []
        for n in lrdu:
            if -1 < n[0] + state[0] < leny and -1 < n[1] + state[1] < lenx:  # eliminate [0,0] fault
                if self.map[n[0] + state[0]][n[1] + state[1]] == 0:
                    emptyCells.append([n[0] + state[0], n[1] + state[1]])
        return emptyCells

    def heuristic(self):
        open_list = [[self.initialState]]   # states to search.
        closed_list = []                    # searched states

        while len(open_list) > 0:           #While there is a new state, get best in open list
            cpath = None
            cpath_heuristic = sys.maxsize #to eliminate the system fault.
            for path in open_list:
                h_n = Map.distance(path[-1], self.goalState) #Heuristic distance between path and goal state.
                if h_n < cpath_heuristic:
                    cpath = h_n
                    cpath = path
            if self.checkGoal(cpath[-1]):
                return cpath

            potential = self.findEmptyCells(cpath[-1])
            n = []
            for s in potential:
                if not s in closed_list:
                    n[:] = cpath  # assign current path to empty variable
                    n.append(s)  # add the chosen coordinate to the empty variable
                    if n in open_list:
                        pass  # already exists
                    else:
                        open_list.append(n)  # add to selectable paths
                    n = []
            closed_list.append(cpath[-1])
            # Let's remove the paths that we can choose so that we don't check a path again.
            open_list.remove(cpath)
        else:
            return None  # no solution available


    def _astar(self):
        open_list = [[self.initialState]]  # states to search.
        closed_list = []  # searched states

        while len(open_list) > 0:
            cpath = None
            cpath_f_n = sys.maxsize
            for path in open_list:
                g_n = len(path)
                h_n = Map.distance(path[-1], self.goalState)
                #print(path[-1])
                f_n = g_n + h_n
                if f_n < cpath_f_n:
                    cpath_f_n = f_n
                    cpath = path
            if self.checkGoal(cpath[-1]):
                return cpath

            potential = self.findEmptyCells(cpath[-1])

            n = []
            for s in potential:
                if not s in closed_list:
                    n[:] = cpath
                    n.append(s)
                    if n in open_list:
                        pass  #We already add it to open list
                    else:
                        open_list.append(n)
                    n = []
            closed_list.append(cpath[-1])
            open_list.remove(cpath)
        else:
            return None

# map, value inverse
"""
for i in range(10):
    for k in range(10):
        if map[i][k]==0:
           map[i][k]=1
        else:
           map[i][k] =0

print(map)

"""

m = Map()
m.getMap(map)
m.robotState([7, 1])  #initial Robot Pose
m.GoalState([1, 8])   #Potential Hider Position 1
path = m.pickAlgorithm('astar')
#path = m.pickAlgorithm('heuristic')
print("Path: ", path, " Path Cost: ", len(path) - 1)
pprint(m.printPath(path))

