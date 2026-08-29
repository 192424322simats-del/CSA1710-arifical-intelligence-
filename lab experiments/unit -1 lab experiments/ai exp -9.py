from itertools import permutations

def tsp(graph, start):

    cities = list(graph.keys())
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    for path in permutations(cities):

        current_path = [start] + list(path) + [start]
        cost = 0

        for i in range(len(current_path) - 1):
            cost += graph[current_path[i]][current_path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = current_path

    print("Shortest Path:", best_path)
    print("Minimum Cost:", min_cost)


# Distance graph
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Main program
tsp(graph, 'A')
