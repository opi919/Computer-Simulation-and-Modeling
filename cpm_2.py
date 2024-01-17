import numpy as np

f = open('cpm_input.txt', 'r')
content = f.read()
numbers = content.split()

# Maximum node
size = 0
for i in range(len(numbers)):
    if i % 3 == 1:
        size = max(size, int(numbers[i]))

# Array_index = node
# Forward[array_index][0] = earliest start
# Forward[array_index][1] = latest finish
forward = np.zeros((size, 2))
print(size)
# Forward pass
no_of_edge = len(numbers) // 3
print(no_of_edge)
for i in range(no_of_edge):
    activity = int(numbers[i * 3 + 2])
    end_node = int(numbers[i * 3 + 1])
    start_node = int(numbers[i * 3])
    print(start_node, end_node, activity)

    if (forward[start_node - 1][1] + activity) > (forward[end_node - 1][1]):
        forward[end_node - 1][0] = forward[start_node - 1][1]
        forward[end_node - 1][1] = forward[end_node - 1][0] + activity

# print('Forward: ', forward)
# Backward[array_index][0] = latest start
# Forward[array_index][1] = latest finish
# Slack[array_index] = slack time
backward = np.zeros((size, 2))
slack = np.zeros(size)

# Backward pass
iteration = no_of_edge - 1
temp = size

backward = np.zeros((size, 2))
max_int_value = np.iinfo(np.int64).max
backward[backward == 0] = 999

backward[size - 1][0] = forward[size - 1][0]
backward[size - 1][1] = forward[size - 1][1]
# backward[size-1][2] = 0 # Slack time of the last node is zero
Temp = no_of_edge - 1
while (temp >= 0):
    temp -= 1
    iteration = no_of_edge - 1
    while (iteration >= 0):
        iteration -= 1
        activity = int(numbers[iteration * 3 + 2])
        end_node = int(numbers[iteration * 3 + 1])
        start_node = int(numbers[iteration * 3])

        if backward[start_node - 1][1] > backward[end_node - 1][0]:
            backward[start_node - 1][1] = backward[end_node - 1][0]
            activity = forward[start_node - 1][1] - forward[start_node - 1][0]
            backward[start_node - 1][0] = backward[start_node - 1][1] - activity

# Calculate Slack Time
for i in range(size):
    slack[i] = backward[i][0] - forward[i][0]

# Critical Path
print('Critical Path: ', end=" ")
for i in range(size):
    if slack[i] == 0:
        print(i + 1, end=" ")
        if i != (size - 1):
            print('->', end=" ")
