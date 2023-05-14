import math

def heuristic(n, goal):
    x1, y1 = n
    x2, y2 = goal
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def astar(graph, start, goal):
    frontier = [(start, 0)]
    explored = []
    while frontier:
        current, cost_so_far = frontier.pop(0)
        if current == goal:
            return cost_so_far
        explored.append(current)
        for neighbor in graph[current]:
            if neighbor not in explored:
                priority = cost_so_far + graph[current][neighbor] + heuristic(neighbor, goal)
                frontier.append((neighbor, priority))
        frontier.sort(key=lambda x: x[1])
    return float('inf')
