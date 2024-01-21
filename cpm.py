def cpm(nodes, activities):
    forward = [0] * nodes
    backward = [float("inf")] * nodes
    slack = [0] * nodes

    # Forward pass
    for i in range(1, nodes + 1):
        for activity in activities:
            if activity[1] == i:
                forward[i - 1] = max(
                    forward[i - 1], forward[activity[0] - 1] + activity[2]
                )

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
    critical_path = []
    for i in range(nodes):
        if slack[i] == 0:
            critical_path.append(i + 1)

    print("Forward:", forward)
    print("Backward:", backward)
    print("Slack:", slack)
    print("Critical Path:", " -> ".join(map(str, critical_path)))

    return critical_path


nodes = 7
# read from file
activities = []
with open("cpm_input.txt") as f:
    for line in f:
        activities.append(tuple(map(int, line.split())))
print(activities)
critical_path = cpm(nodes, activities)
