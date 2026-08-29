import heapq

def a_star(graph, heuristic, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost = {start: 0}

    while open_list:

        current_f, current = heapq.heappop(open_list)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path, cost[goal]

        for neighbour, distance in graph[current]:

            new_cost = cost[current] + distance

            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                f_cost = new_cost + heuristic[neighbour]

                heapq.heappush(
                    open_list,
                    (f_cost, neighbour)
                )

                came_from[neighbour] = current

    return None, float('inf')


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('D', 1)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'G': 0
}

# Main program
path, cost = a_star(graph, heuristic, 'A', 'G')

print("Shortest Path:", path)
print("Total Cost:", cost)
