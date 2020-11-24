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
    startPoint = problem.getStartState()
    explored = []
    explored.append(startPoint)
    fringe = util.Stack()                           #Implement a stack for the search
    fringe.push((startPoint, []))
    while not fringe.isEmpty():                     #Search continues until each successor is searched
        state, path = fringe.pop()
        if problem.isGoalState(state):              #Returns the path to the goal
            return path
        explored.append(state)                      #Mark the current coordinates as explored
        successor = problem.getSuccessors(state)
        for i in successor:                         #For loop used to iterate through each successor
            coordinates = i[0]
            direction = i[1]
            if coordinates not in explored:         #If statement used to stop repeated searches
                fringe.push((coordinates, path + [direction]))
    return path + [direction]                       #Return the successor's path
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    startPoint = problem.getStartState()
    explored = []
    explored.append(startPoint)
    fringe = util.Queue()                           #Implement a queue for the search
    fringe.push((startPoint, []))
    while not fringe.isEmpty():                     #Search continues until each successor is searched
        state, path = fringe.pop()
        if problem.isGoalState(state):              #Returns the path to the goal
            return path
        successor = problem.getSuccessors(state)
        for i in successor:                         #For loop used to iterate each successor
            coordinates = i[0]
            if coordinates not in explored:         #If statement used to stop repeated searches
                direction = i[1]
                fringe.push((coordinates, path + [direction]))
                explored.append(coordinates)        #Mark the successor's coordinates as explored
    return path                                     #Returns the current path
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startPoint = problem.getStartState()
    explored = []
    fringe = util.PriorityQueue()                   #Implement a priority queue for the search
    fringe.push((startPoint, []), 0)
    while not fringe.isEmpty():                     #Search continues until each successor is searched
        state, path = fringe.pop()
        if problem.isGoalState(state):              #Returns the path to the goal
            return path
        if state not in explored:                   #Check if the state has been explored already, to allow the least
            successor = problem.getSuccessors(state)#cost to be searched first
            for i in successor:
                coordinates = i[0]
                if coordinates not in explored:     #If statement prevents explored successors from being searched
                    direction = i[1]
                    fringe.push((coordinates, path + [direction]), problem.getCostOfActions(path + [direction]))
                    explored.append(state)          #Mark the current state as explored
    return path                                     #Returns the current path
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
    startPoint = problem.getStartState()
    explored = []
    fringe = util.PriorityQueue()                       #Implement a priority queue for the state graph
    fringe.push((startPoint, []), heuristic(startPoint, problem))
    while not fringe.isEmpty():                         #A* searches each successor until all states are checked
        state, path = fringe.pop()
        if problem.isGoalState(state):                  #Check if we have arrived at the end, and return our path
            return path
        if state not in explored:                       #Prevents the search from repeating a search
            successors = problem.getSuccessors(state)
            for i in successors:                        #Insert each successor into the fringe
                coordinates = i[0]
                if coordinates not in explored:         #Prevents the search from pushing duplicates into the fringe
                    direction = i[1]
                    fringe.push((coordinates, path + [direction]), problem.getCostOfActions(path + [direction]) + heuristic(coordinates, problem))
                    explored.append(state)              #Marks the current coordinates as explored
    return path
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
