# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    startStateTuple = tuple([startState, "Start", 0])
    currentState = startStateTuple
    openStack = util.Stack()
    closedSet = set([])
    parentDict = {}
    while not (problem.isGoalState(currentState[0])):
        if currentState[0] in closedSet and not openStack.isEmpty() :
            currentState = openStack.pop()
        closedSet.add(currentState[0])
        for successor in problem.getSuccessors(currentState[0]):
            if successor[0] not in closedSet:
                openStack.push(successor)
                parentDict[successor] = currentState
        if not openStack.isEmpty():
            currentState = openStack.pop()
    directionList = []
    currentReturn = currentState
    while currentReturn != startStateTuple:
        directionList.append(currentReturn[1])
        currentReturn = parentDict.get(currentReturn)
    directionList.reverse()
    return directionList
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    currentStateTriple = tuple([currentState, "Start", 0])
    startStateTuple = currentStateTriple
    openQueue = util.Queue()
    closedList = []
    parentDict = {}
    while not (problem.isGoalState(currentState)):
        if (currentState in closedList) and (not openQueue.isEmpty()):
            currentStateTriple = openQueue.pop()
            currentState = currentStateTriple[0]
        if not problem.isGoalState(currentState):
            closedList.append(currentState)
            for successor in problem.getSuccessors(currentState):
                if successor[0] not in closedList:
                    if not isinstance(currentStateTriple[0][0], int) and not isinstance(currentStateTriple[0][0], str):
                        if not isinstance(currentStateTriple[0][1], tuple) and not isinstance(currentStateTriple[0][1], list):
                            if isinstance(currentStateTriple[0][1][0], list):
                                tupledTuplesSuccessor = tuple(tuple(x) for x in successor[0][1])
                                tupledTuplesParent = tuple(tuple(x) for x in currentStateTriple[0][1])
                                successorTuple = ((successor[0][0], tupledTuplesSuccessor), successor[1], successor[2])
                                currentStateParentTuple = ((currentStateTriple[0][0], tupledTuplesParent), currentStateTriple[1],currentStateTriple[2])
                            else:
                                successorTuple = ((successor[0][0], tuple(successor[0][1])), successor[1], successor[2])
                                currentStateParentTuple = ((currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1],currentStateTriple[2])
                        else:
                            successorTuple = ((successor[0][0], tuple(successor[0][1])), successor[1], successor[2])
                            currentStateParentTuple = (
                            (currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1],
                            currentStateTriple[2])
                    else:
                        successorTuple = successor
                        currentStateParentTuple = (currentStateTriple[0], currentStateTriple[1], currentStateTriple[2])
                    parentDict[successorTuple] = currentStateParentTuple
                    openQueue.push(successor)
            if not openQueue.isEmpty():
                currentStateTriple = openQueue.pop()
                currentState = currentStateTriple[0]
    directionList = []
    if not isinstance(currentStateTriple[0][0], int) and not isinstance(currentStateTriple[0][0], str):
        if not isinstance(currentStateTriple[0][1], tuple) and not isinstance(currentStateTriple[0][1], list):
            if isinstance(currentStateTriple[0][1][0], list):
                tupledTuplesReturn = tuple(tuple(x) for x in currentStateTriple[0][1])
                tupledTuplesStart = tuple(tuple(x) for x in startStateTuple[0][1])
                currentReturn = ((currentStateTriple[0][0], tupledTuplesReturn), currentStateTriple[1], currentStateTriple[2])
                startStateTuple = ((startStateTuple[0][0], tupledTuplesStart), startStateTuple[1], startStateTuple[2])
            else:
                currentReturn = ((currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1], currentStateTriple[2])
                startStateTuple = ((startStateTuple[0][0], tuple(startStateTuple[0][1])), startStateTuple[1], startStateTuple[2])
        else:
            currentReturn = (
            (currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1], currentStateTriple[2])
            startStateTuple = (
            (startStateTuple[0][0], tuple(startStateTuple[0][1])), startStateTuple[1], startStateTuple[2])
    else:
        currentReturn = currentStateTriple
    while currentReturn != startStateTuple:
        directionList.append(currentReturn[1])
        currentReturn = parentDict.get(currentReturn)
    directionList.reverse()
    return directionList
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    startState = problem.getStartState()
    startStateTuple = tuple([startState, "Start", 0])
    currentState = startStateTuple
    openPQ = util.PriorityQueue()
    closedSet = set([])
    parentDict = {}
    costDict = {currentState: 0}
    while not (problem.isGoalState(currentState[0])):
        if (currentState[0] in closedSet) and (not openPQ.isEmpty()):
            currentState = openPQ.pop()
        if not problem.isGoalState(currentState[0]):
            closedSet.add(currentState[0])
            for successor in problem.getSuccessors(currentState[0]):
                if successor[0] not in closedSet:
                    parentDict[successor] = currentState
                    costDict[successor] = costDict.get(currentState) + successor[2]
                    openPQ.push(successor, costDict.get(successor))
            if not openPQ.isEmpty():
                currentState = openPQ.pop()
    directionList = []
    currentReturn = currentState
    while currentReturn != startStateTuple:
        directionList.append(currentReturn[1])
        currentReturn = parentDict.get(currentReturn)
    directionList.reverse()
    return directionList
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    currentState = problem.getStartState()
    currentStateTriple = tuple([currentState, "Start", 0])
    startStateTuple = currentStateTriple
    openPQ = util.PriorityQueue()
    closedList = []
    parentDict = {}
    if not isinstance(currentStateTriple[0][0], int) and not isinstance(currentStateTriple[0][0], str):
        if not isinstance(currentStateTriple[0][1], tuple) and not isinstance(currentStateTriple[0][1], list):
            if isinstance(currentStateTriple[0][1][0], list):
                tupledTuples = tuple(tuple(x) for x in currentStateTriple[0][1])
                currentStateTupledList = ((currentStateTriple[0][0], tupledTuples), currentStateTriple[1], currentStateTriple[2])
            else:
                currentStateTupledList = ((currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1],currentStateTriple[2])
        else:
            currentStateTupledList = ((currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1], currentStateTriple[2])
    else:
        currentStateTupledList = currentStateTriple
    costDict = {currentStateTupledList: 0}
    while not (problem.isGoalState(currentState)):
        if (currentState in closedList) and (not openPQ.isEmpty()):
            currentStateTriple = openPQ.pop()
            currentState = currentStateTriple[0]
        if not problem.isGoalState(currentState):
            closedList.append(currentState)
            for successor in problem.getSuccessors(currentState):
                if successor[0] not in closedList:
                    if not isinstance(currentStateTriple[0][0], int) and not isinstance(currentStateTriple[0][0], str):
                        if not isinstance(currentStateTriple[0][1], tuple) and not isinstance(currentStateTriple[0][1], list):
                            if isinstance(currentStateTriple[0][1][0], list):
                                tupledTuplesSuccessor = tuple(tuple(x) for x in successor[0][1])
                                tupledTuplesParent = tuple(tuple(x) for x in currentStateTriple[0][1])
                                successorTuple = ((successor[0][0], tupledTuplesSuccessor), successor[1], successor[2])
                                currentStateParentTuple = ((currentStateTriple[0][0], tupledTuplesParent), currentStateTriple[1],currentStateTriple[2])
                            else:
                                successorTuple = ((successor[0][0], tuple(successor[0][1])), successor[1], successor[2])
                                currentStateParentTuple = ((currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1],currentStateTriple[2])
                        else:
                            successorTuple = ((successor[0][0], tuple(successor[0][1])), successor[1], successor[2])
                            currentStateParentTuple = (
                            (currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1],
                            currentStateTriple[2])
                    else:
                        successorTuple = successor
                        currentStateParentTuple = (currentStateTriple[0], currentStateTriple[1], currentStateTriple[2])
                    parentDict[successorTuple] = currentStateParentTuple
                    costDict[successorTuple] = costDict.get(currentStateParentTuple) + successorTuple[2] + heuristic(successorTuple[0],problem) - heuristic(currentStateParentTuple[0], problem)
                    openPQ.push(successor, costDict[successorTuple])
            if not openPQ.isEmpty():
                currentStateTriple = openPQ.pop()
                currentState = currentStateTriple[0]
    directionList = []
    if not isinstance(currentStateTriple[0][0], int) and not isinstance(currentStateTriple[0][0], str):
        if not isinstance(currentStateTriple[0][1], tuple) and not isinstance(currentStateTriple[0][1], list):
            if isinstance(currentStateTriple[0][1][0], list):
                tupledTuplesReturn = tuple(tuple(x) for x in currentStateTriple[0][1])
                tupledTuplesStart = tuple(tuple(x) for x in startStateTuple[0][1])
                currentReturn = ((currentStateTriple[0][0], tupledTuplesReturn), currentStateTriple[1], currentStateTriple[2])
                startStateTuple = ((startStateTuple[0][0], tupledTuplesStart), startStateTuple[1], startStateTuple[2])
            else:
                currentReturn = ((currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1], currentStateTriple[2])
                startStateTuple = ((startStateTuple[0][0], tuple(startStateTuple[0][1])), startStateTuple[1], startStateTuple[2])
        else:
            currentReturn = (
            (currentStateTriple[0][0], tuple(currentStateTriple[0][1])), currentStateTriple[1], currentStateTriple[2])
            startStateTuple = (
            (startStateTuple[0][0], tuple(startStateTuple[0][1])), startStateTuple[1], startStateTuple[2])
    else:
        currentReturn = currentStateTriple
    while currentReturn != startStateTuple:
        directionList.append(currentReturn[1])
        currentReturn = parentDict.get(currentReturn)
    directionList.reverse()
    return directionList
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
