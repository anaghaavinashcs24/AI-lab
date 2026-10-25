
import heapq

def manhattan(state, goal):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3)
            distance += abs(i % 3 - j % 3)

    return distance


def solvable(state):
    nums = [x for x in state if x != 0]
    inversions = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inversions += 1

    return inversions % 2 == 0


def astar(start, goal):
    pq = []
    heapq.heappush(
        pq, (manhattan(start, goal), 0, start)
    )

    cost = {start: 0}
    parent = {start: None}

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        if state == goal:
            path = []
            current = state

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nSolution path:")
            for step, s in enumerate(path):
                print("Step", step)
                for i in range(0, 9, 3):
                    print(s[i:i + 3])
                print()

            print("Total moves:", len(path) - 1)
            return

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        moves = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc
                new_state = list(state)

                new_state[zero], new_state[new_zero] = (
                    new_state[new_zero], new_state[zero]
                )

                new_state = tuple(new_state)
                new_g = g + 1

                if new_g < cost.get(new_state, float("inf")):
                    cost[new_state] = new_g
                    parent[new_state] = state
                    new_f = new_g + manhattan(new_state, goal)

                    heapq.heappush(
                        pq, (new_f, new_g, new_state)
                    )

    print("No solution")


# Main program
start = tuple(map(
    int, input("Enter start state (9 numbers, use 0 for blank): ").split()
))

goal = tuple(map(
    int, input("Enter goal state (9 numbers): ").split()
))

if (len(start) != 9 or len(goal) != 9
        or sorted(start) != list(range(9))
        or sorted(goal) != list(range(9))):
    print("Invalid input")

elif not solvable(start) or not solvable(goal):
    print("Puzzle is not solvable")

else:
    astar(start, goal)
