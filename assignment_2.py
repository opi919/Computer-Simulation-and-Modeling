def cpm(nodes, activities):
    forward = [0] * nodes
    backward = [float('inf')] * nodes
    slack = [0] * nodes

    # Forward pass
    for i in range(1, nodes + 1):
        for activity in activities:
            if activity[1] == i:
                forward[i - 1] = max(forward[i - 1], forward[activity[0] - 1] + activity[2])

    # Backward pass
    backward[-1] = forward[-1]
    for i in range(nodes - 2, -1, -1):
        for activity in activities:
            if activity[0] == i + 1:
                backward[i] = min(backward[i], backward[activity[1] - 1] - activity[2])

    # Calculate slack time
    for i in range(nodes):
        slack[i] = backward[i] - forward[i]

    # Identify critical path
    critical_path = [i + 1 for i in range(nodes) if slack[i] == 0]

    print("Forward:", forward)
    print("Backward:", backward)
    print("Slack:", slack)
    print("Critical Path:", " -> ".join(map(str, critical_path)))

    return critical_path


nodes = 7
activities = [(1, 2, 11), (1, 3, 3), (1, 4, 10), (4, 5, 3), (3, 5, 1), (2, 6, 2), (5, 6, 1), (6, 7, 1)]
critical_path = cpm(nodes, activities)
