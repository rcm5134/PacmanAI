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
import game
import pacman
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
    return [s, s, w, s, w, w, s, w]

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

    # Set of nodes already expanded
    expanded = set()
    # LIFO stack to represent the fringe
    stack = util.Stack()
    # Initial state of the start state and no actions taken
    start_state = (problem.getStartState(), [])

    stack.push(start_state)
    # Continue while the stack is not empty
    while not stack.isEmpty():
        # Get the deepest node
        curr_node = stack.pop()
        # Catch the current state and current path
        curr_state = curr_node[0]
        curr_path = curr_node[1]
        # Ignore the node if its already expanded
        if curr_state not in expanded:
            # Mark this node as expanded
            expanded.add(curr_state)
            # Check if it's a goal state
            if problem.isGoalState(curr_state):
                return curr_path
            # Push each successor as a state and a total path taken so far
            for successor in problem.getSuccessors(curr_state):
                stack.push((successor[0], curr_path + [successor[1]]))

    # there is no possible path to the goal node
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    # Set of nodes already expanded
    expanded = set()
    # FIFO queue to represent the fringe
    queue = util.Queue()
    # Initial state of the start state and no actions taken
    start_state = (problem.getStartState(), [])

    curr_path = []

    queue.push(start_state)
    # Continue while the stack is not empty
    while not queue.isEmpty():
        # Get the shallowest node
        curr_node = queue.pop()
        # Catch the current state and current path
        curr_state = curr_node[0]
        curr_path = curr_node[1]
        # Ignore the node if its already expanded
        if curr_state not in expanded:
            # Mark this node as expanded
            expanded.add(curr_state)
            # Check if it's a goal state
            if problem.isGoalState(curr_state):
                return curr_path
            # Push each successor as a state and a total path taken so far
            for successor in problem.getSuccessors(curr_state):
                queue.push((successor[0], curr_path + [successor[1]]))

    # there is no possible path to the goal node
    return curr_path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    expanded = set()
    # Priority queue used to manage the fringe, prioritizing the lowest cost move
    p_queue = util.PriorityQueue()
    # Initial state of the start state and no actions taken
    start_state = [problem.getStartState(), [], 0]
    # Push the initial state
    p_queue.push(start_state, start_state[2])

    while not p_queue.isEmpty():
        curr_node = p_queue.pop()

        # Catch the current state and current path and cumulative cost so far
        curr_state = curr_node[0]
        curr_path = curr_node[1]
        total_cost = curr_node[2]

        # Ignore the node if its already expanded
        if curr_state not in expanded:
            # Mark this node as expanded
            expanded.add(curr_state)
            # Check if it's a goal state
            if problem.isGoalState(curr_state):
                return curr_path
            # Push each successor as a state and a total path taken so far and total cost so far
            for successor in problem.getSuccessors(curr_state):

                p_queue.push([successor[0], curr_path + [successor[1]], total_cost + successor[2]],
                             total_cost + successor[2])

    # there is no possible path to the goal node
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    expanded = set()
    # Priority queue used to manage the fringe, prioritizing the lowest cost move
    p_queue = util.PriorityQueue()
    # Initial state of the start state and no actions taken
    start_state = [problem.getStartState(), [], 0]
    # Push the initial state
    p_queue.push(start_state, start_state[2])

    while not p_queue.isEmpty():
        curr_node = p_queue.pop()
        # Catch the current state and current path and cumulative cost so far
        curr_state = curr_node[0]
        curr_path = curr_node[1]
        total_cost = curr_node[2]

        # Ignore the node if its already expanded
        if curr_state not in expanded:
            # Mark this node as expanded
            expanded.add(curr_state)
            # Check if it's a goal state
            if problem.isGoalState(curr_state):
                return curr_path
            # Push each successor as a state and a total path taken so far and total cost so far plus a heuristic value
            for successor in problem.getSuccessors(curr_state):
                p_queue.push([successor[0], curr_path + [successor[1]], total_cost + successor[2]],
                             total_cost + successor[2] + heuristic(successor[0], problem))

    # there is no possible path to the goal node
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
