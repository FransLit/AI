# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    paths = []
    moves = []
    branches = []

    nextstate = problem.getStartState()
    paths.append(nextstate)
    
    def goforward(paths, moves, nextstate, branches):
            if problem.isGoalState(nextstate):
                print("Found!!!!")
            else:
                path_found = False
                for i in reversed(range(len(problem.getSuccessors(nextstate)))):
                    if problem.getSuccessors(nextstate)[i][0] not in paths:
                        paths.append(problem.getSuccessors(nextstate)[i][0])
                        print(problem.getSuccessors(nextstate))
                        temp = problem.getSuccessors(nextstate)[i][1]
                        temp2 = nextstate
                        nextstate = problem.getSuccessors(nextstate)[i][0]
                        temp3 = list(moves)
                        moves.append(temp)
                        for i in range(len(problem.getSuccessors(temp2))):
                            temp4 = list(temp3)
                            if problem.getSuccessors(temp2)[i][0] not in paths and problem.getSuccessors(temp2)[i][0] != nextstate:
                                temp4.append(problem.getSuccessors(temp2)[i][1])
                                branches.append([problem.getSuccessors(temp2)[i][0],temp4])
                        path_found = True

                        break
                if path_found == False and branches != []:
                    nextstate = branches[-1][0]
                    moves = branches[-1][1]
                    branches.pop(-1)
            
            return paths, moves, nextstate, branches
    
    while problem.isGoalState(nextstate) == False:
        paths, moves, nextstate, branches = goforward(paths, moves, nextstate, branches)
    
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #print("Successors: ", problem.getSuccessors((34, 15)))
    
    return moves

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    discovered = []
    queue = util.Queue()
    next_queue = util.Queue()
    pathFound = False

    startstate = problem.getStartState()
    discovered.append(startstate)
    if problem.isGoalState(startstate):
        return []
    successors = problem.getSuccessors(startstate)
    for i in successors:
        queue.push((i[0], [i[1]], i[2]))

    while not pathFound:
        if not queue.isEmpty():
            state, path, path_cost = queue.pop()
            if problem.isGoalState(state):
                pathFound = True
                print(path_cost)
                return path
            else:
                if state not in discovered:
                    discovered.append(state)
                    successors = problem.getSuccessors(state)
                    for state, action, cost in successors:
                        next_queue.push((state, path + [action], path_cost + cost))
        else:
            for i in reversed(next_queue.list):
                queue.push(i)
            next_queue.list = []

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
