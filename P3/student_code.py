import heapq
import math

def step_cost(intersection_1, intersection_2):
    x1, y1 = intersection_1
    x2, y2 = intersection_2
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )


def h(M, start, goal):
    return step_cost(M.intersections[start], M.intersections[goal])

def shortest_path(M,start,goal):
    if start == goal:
        return [start]

    explored = set()

    heuristics = dict()
    for node in M.intersections.keys():
        heuristics[node] = h(M, node, goal)

    step_cost_dict = dict()   
     
    frontier = [(0, 0, 0, [start])]
    goal_path = None
    _id = 1
    while frontier:
        cost, _, current_path_costs, path = heapq.heappop(frontier)
        explored.add(path[-1])
        
        if goal_path:
            if goal_path[0] < cost:
                break
            
        nodes = M.roads[path[-1]]
        for node in nodes:
            new_path = path + [node]
            step_str = "{},{}".format(str(path[-1]), str(node))
            if step_str not in step_cost_dict:
                step_cost_dict[step_str] = step_cost(M.intersections[path[-1]], M.intersections[node])
            if node == goal:
                p_cost = current_path_costs + step_cost_dict[step_str]

                if not goal_path:
                    goal_path = (p_cost, new_path)
                else:
                    if goal_path[0] > p_cost:
                        goal_path = (p_cost, new_path)

            elif node not in explored:
                p_cost = current_path_costs + step_cost_dict[step_str]
                node_cost = p_cost + heuristics[node]
                heapq.heappush(frontier, (node_cost, _id, p_cost, new_path))
                _id += 1
                   

    return goal_path[1] if goal_path else []