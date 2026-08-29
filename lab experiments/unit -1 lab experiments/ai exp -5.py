from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    # Check left bank
    if m_left < 0 or c_left < 0:
        return False

    if m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and m_left < c_left:
        return False

    # Check right bank
    if m_right > 0 and m_right < c_right:
        return False

    return True


def solve_missionaries_cannibals():

    # State = (missionaries_left, cannibals_left, boat_side)
    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque()
    queue.append((start, []))

    visited = set()

    # Possible boat movements
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    while queue:

        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        path = path + [state]

        if state == goal:
            print("Solution Steps:")
            for step in path:
                print(step)
            return

        m_left, c_left, boat = state

        for m, c in moves:

            if boat == 0:
                # Boat moves from left to right
                new_m = m_left - m
                new_c = c_left - c
                new_boat = 1
            else:
                # Boat moves from right to left
                new_m = m_left + m
                new_c = c_left + c
                new_boat = 0

            new_state = (
                new_m,
                new_c,
                new_boat
            )

            m_right = 3 - new_m
            c_right = 3 - new_c

            if is_valid(new_m, new_c, m_right, c_right):
                if new_state not in visited:
                    queue.append((new_state, path))


# Main program
solve_missionaries_cannibals()
