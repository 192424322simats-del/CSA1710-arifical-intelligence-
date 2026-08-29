from collections import deque

def water_jug(jug1, jug2, target):

    visited = set()
    queue = deque()

    # Initial state
    queue.append((0, 0, []))

    while queue:

        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        path = path + [(a, b)]

        # Check target
        if a == target or b == target:
            print("Solution Steps:")
            for step in path:
                print(step)
            return

        # Possible operations
        states = [
            (jug1, b),              # Fill Jug 1
            (a, jug2),              # Fill Jug 2
            (0, b),                 # Empty Jug 1
            (a, 0),                 # Empty Jug 2
            (a - min(a, jug2-b),    # Pour Jug 1 -> Jug 2
             b + min(a, jug2-b)),
            (a + min(b, jug1-a),    # Pour Jug 2 -> Jug 1
             b - min(b, jug1-a))
        ]

        for state in states:
            if state not in visited:
                queue.append((state[0], state[1], path))


# Main program
jug1 = 4
jug2 = 3
target = 2

water_jug(jug1, jug2, target)
