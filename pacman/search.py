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
import heapq

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


def depthFirstSearch(problem):

    stack = []
    start = (problem.getStartState(), None, 0)
    stack.append(start)
    actions = []
    help = dict()
    help[start] = None
    target = problem.getStartState()
    explored = set()
    explored.add(problem.getStartState())
    while stack:
        current_state = stack.pop()
        explored.add(current_state[0])
        if problem.isGoalState(current_state[0]):
            target = current_state
            break
        for succ in problem.getSuccessors(current_state[0]):
            if succ[0] not in explored:
                help[succ] = current_state
                stack.append(succ)

    while target is not None:
        actions.append(target[1])
        target = help[target]
    actions.reverse()
    actions.remove(None)

    return actions


def breadthFirstSearch(problem):

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def uniformCostSearch(problem):
    priority_queue = [(0, (problem.getStartState(), None, 0))]
    help = {(problem.getStartState(),None,0): (0, None)}
    while priority_queue:
        target_cost,target_node = heapq.heappop(priority_queue)

        if problem.isGoalState(target_node[0]):
            target = target_node
            actions=[]
            while target is not None:
                actions.append(target[1])
                target = help[target][1]
            actions.reverse()
            actions.remove(None)
            return actions

        for successor in problem.getSuccessors(target_node[0]):
            new_cost = target_cost + successor[2]
            if new_cost < target_cost or successor not in help:
                help[successor] = (new_cost, target_node)
                heapq.heappush(priority_queue, (new_cost, successor))

    return None


def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    frontier = util.PriorityQueue()
    start = problem.getStartState()

    # هر عنصر: (state, path, cost)
    frontier.push((start, [], 0), heuristic(start, problem))

    visited = {}

    while not frontier.isEmpty():

        state, path, cost = frontier.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited or cost < visited[state]:
            visited[state] = cost

            for successor, action, stepCost in problem.getSuccessors(state):

                new_cost = cost + stepCost
                new_path = path + [action]
                priority = new_cost + heuristic(successor, problem)

                frontier.push((successor, new_path, new_cost), priority)

    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
