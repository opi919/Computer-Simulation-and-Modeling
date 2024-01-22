class Activity:
    def __init__(self, name, duration) -> None:
        self.name = name
        self.duration = duration
        self.predecessors = []
        self.successors = []
        self.es = 0
        self.ef = 0
        self.ls = 0
        self.lf = 0
        self.st = 0


file_name = "precedence.txt"

activities = {}

with open(file_name, 'r') as file:
    for line in file:
        name, *rest = line.strip().split()
        duration = int(rest[0])
        predecessors = [] if len(rest) == 1 else rest[1].split(",")

        activities[name] = Activity(name, duration)
        activities[name].predecessors = predecessors

        for predecessor in predecessors:
            activities[predecessor].successors.append(name)

max_earliest_finish = 0

for name, activity in activities.items():
    if not activity.predecessors:
        activity.ef = activity.duration
    else:
        max_earliest_start = max(activities[pre].ef for pre in activity.predecessors)
        activity.es = max_earliest_start
        activity.ef = max_earliest_start + activity.duration

    max_earliest_finish = max(max_earliest_finish, activity.ef)

for name in reversed(activities):
    activity = activities[name]
    if not activity.successors:
        activity.lf = max_earliest_finish
        activity.ls = max_earliest_finish - activity.duration
    else:
        min_latest_start = min(activities[suc].ls for suc in activity.successors)
        activity.lf = min_latest_start
        activity.ls = min_latest_start - activity.duration

    activity.st = activity.ls - activity.es

    critical_path = ""

for name, activity in activities.items():
    print(
        f"{name} -> ES: {activity.es} EF: {activity.ef} LS: {activity.ls} LF: {activity.lf} ST: {activity.st}"
    )
    if activity.st == 0:
        critical_path += name + " -> "

print(f"\nCritical Path: {critical_path[:-4]}")
