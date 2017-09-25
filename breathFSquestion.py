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


def breadthFirstSearchComplete(problem):
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
