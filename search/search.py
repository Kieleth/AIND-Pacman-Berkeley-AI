# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

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
  [2nd Edition: p 75, 3rd Edition: p 87]

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
        successors.append( ( nextState, action, cost) )
  """
  "*** YOUR CODE HERE ***"
  frontier = util.Stack()
  start_node = problem.getStartState()

  if problem.isGoalState(start_node):
      return ['Stop']
  frontier.push((start_node,[]))
  explored = set()
  while True:
      if frontier.isEmpty():
          return []
      node = frontier.pop()
      explored.add(node[0])
      for successor in problem.getSuccessors(node[0]):
          nextState, action, cost = successor
          if nextState in explored or nextState in [f[0] for f in frontier.list]:
              continue
          actions = node[1][:]
          actions.append(action)
          new_node = (nextState, actions)
          if problem.isGoalState(new_node[0]):
              return new_node[1]
          frontier.push(new_node)
          #print frontier.list
  return []


def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  #import pdb;pdb.set_trace()
  frontier = util.Queue()
  start_node = problem.getStartState()
  if problem.isGoalState(start_node):
      return ['Stop']
  frontier.push((start_node,()))
  explored = set()
  while True:
      if frontier.isEmpty():
          return []
      node = frontier.pop()

      explored.add(node[0])
      # exploratory code for SUPER-optimal solution:
      # by saving the path in explored, we assure that we explore the same cell even if
      # two different actions go through it:
      #explored.add(node)
      for successor in problem.getSuccessors(node[0]):
          nextState, action, cost = successor
          if nextState in explored or nextState in [f[0] for f in frontier.list]:
              continue
          actions = node[1]
          next_actions = actions + (action,)
          new_node = (nextState, next_actions)
          if problem.isGoalState(new_node[0]):
              return new_node[1]
          frontier.push(new_node)
          #print frontier.list
  return []


def breadthFirstSearchPaths(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  #import pdb;pdb.set_trace()
  frontier = util.Queue()
  start_node = problem.getStartState()
  if problem.isGoalState(start_node):
      return ['Stop']
  frontier.push((start_node,()))
  explored = set()
  while True:
      if frontier.isEmpty():
          return []
      node = frontier.pop()

      #explored.add(node[0])
      # exploratory code for SUPER-optimal solution:
      # by saving the path in explored, we assure that we explore the same cell even if
      # two different actions go through it:
      explored.add(node)
      for successor in problem.getSuccessors(node[0]):
          nextState, action, cost = successor
          if nextState in explored or nextState in [f[0] for f in frontier.list]:
              continue
          actions = node[1]
          next_actions = actions + (action,)
          new_node = (nextState, next_actions)
          if problem.isGoalState(new_node[0]):
              return new_node[1]
          frontier.push(new_node)
          #print frontier.list
  return []


def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  """ Time lost here, cause I was trying to hack into the cost function
      only to find out that the cost is actually returned by getSuccessors!!!!!!!
      SO>>piped the cost into the priority, and all good
  """
  def fun(item):
      """ Less is more
          accepts (node, [path, ...])
      """
      node, path = item
      value = len(path)

      if node in problem.food:
          value -= 20

      return value

  frontier = util.PriorityQueue()
  start_node = problem.getStartState()
  if problem.isGoalState(start_node):
      return ['Stop']
  frontier.push((start_node, []), problem.costFn(start_node))
  explored = set()
  while True:
      if frontier.isEmpty():
          return []
      node = frontier.pop()
      # This actually checks 'after' we've done frontier exapansion, so we're sure of getting optimal solution
      if problem.isGoalState(node[0]):
          return node[1]
      explored.add(node[0])
      for successor in problem.getSuccessors(node[0]):
          nextState, action, cost = successor
          #import pdb;pdb.set_trace()
          #if nextState in [f[1][0] for f in frontier.heap]:


          if nextState in explored:
              continue
          # f[1][0] is an (priority, element) 'element' in heap, and then the element itself for element[0] and not the path element[1]

          actions = node[1][:]
          actions.append(action)
          new_node = (nextState, actions)
          frontier.push(new_node, cost)
          #print frontier.list
  return []


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearchO(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  frontier = util.PriorityQueue()
  start_node = problem.getStartState()
  if problem.isGoalState(start_node):
      return ['Stop']
  frontier.push((start_node, []), heuristic(start_node, problem))
  explored = set()
  while True:
      if frontier.isEmpty():
          return []
      node = frontier.pop()
      # This actually checks 'after' we've done frontier exapansion, so we're sure of getting optimal solution
      if problem.isGoalState(node[0]):
          return node[1]
      explored.add(node[0])
      #import pdb;pdb.set_trace()
      for successor in problem.getSuccessors(node[0]):
          nextState, action, cost = successor
          #if nextState in [f[1][0] for f in frontier.heap]:

          if nextState in explored:
              continue
          # f[1][0] is an (priority, element) 'element' in heap, and then the element itself for element[0] and not the path element[1]

          actions = node[1][:]
          actions.append(action)
          new_node = (nextState, actions)
          #frontier.push(new_node, heuristic(nextState, problem))
          # "Proper" A* with cost function cost + heuristic, opens many nodes 16K!
          # Compared with 'just heuristic here, of 400 nodes
          frontier.push(new_node, len(actions) +  heuristic(nextState, problem))
          #print frontier.list
  return []


def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  frontier = util.PriorityQueue()
  start_node = problem.getStartState()
  if problem.isGoalState(start_node):
      return ['Stop']
  frontier.push((start_node, ()), heuristic(start_node, problem))
  # We use a hash table to keep the smalles of the paths to a state
  explored = dict()
  while True:
      if frontier.isEmpty():
          return []
      node = frontier.pop()
      # This actually checks 'after' we've done frontier exapansion, so we're sure of getting optimal solution
      if problem.isGoalState(node[0]):
          return node[1]
      explored[node[0]] = node[1]

      #import pdb;pdb.set_trace()
      for successor in problem.getSuccessors(node[0]):
          nextState, action, cost = successor

          actions = node[1][:]
          actions = actions + (action, )

          if nextState in explored:
              continue

          # This Frontier check works by comparing the len of the actions that have led to a an State.
          # Doing this, we can discard those successors that are not good enough for a solution early.
          actions_if_in_explored = explored.get(nextState)
          if actions_if_in_explored and len(actions_if_in_explored) < len(actions):
              continue
          else:
              explored[nextState] = actions

          new_node = (nextState, actions)
          frontier.push(new_node, len(actions) +  heuristic(nextState, problem))
          #print frontier.list
  return []


# Abbreviations
bfs = breadthFirstSearch
bfsp = breadthFirstSearchPaths
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
