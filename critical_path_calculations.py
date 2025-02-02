# -*- coding: utf-8 -*-
"""Critical Path Calculations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hm1TmxGw0liA0Pu1JkOJBxDd0WtBmUzP
"""

from pulp import *

"""Best Case Scenario"""

# Create a dictionary of the activities and their durations
activitiesBest = {
    'A': 2,
    'B': 4,
    'C': 4,
    'D1': 8,
    'D2': 24,
    'D3': 24,
    'D4': 40,
    'D5': 8,
    'D6': 10,
    'D7': 10,
    'D8': 4,
    'E': 24,
    'F': 4,
    'G': 12,
    'H': 8

}
# Create a list of the activities
activities_list = list(activitiesBest.keys())
# Create a dictionary of the activity precedences
precedences = {
    'A': [],
    'B': [],
    'C': ['A'],
    'D1': ['A'],
    'D2': ['D1'],
    'D3': ['D1'],
    'D4': ['D2', 'D3'],
    'D5': ['D4'],
    'D6': ['D4'],
    'D7': ['D6'],
    'D8': ['D5', 'D7'],
    'E': ['B', 'C'],
    'F': ['D8', 'E'],
    'G': ['A', 'D8'],
    'H': ['F', 'G']
    }



# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in
activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in
activities_list}

# Add the constraints
for activity in activities_list:
    # Duration constraint: end time = start time + duration
    prob += end_times[activity] == start_times[activity] + activitiesBest[activity], f"{activity}_duration"

    # Precedence constraints: start time should be after the end time of predecessors
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"
# Solve the LP problem
status = prob.solve()
# Print the results
print("Critical Path time:")
for activity in activities_list:
    print(f"{activity} starts at {value(start_times[activity])} hours and ends at {value(end_times[activity])} hours")

if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
    print(f"{activity} ends at {value(end_times[activity])} hours in duration")

"""Expected Case"""

# Create a dictionary of the activities and their durations
activitiesExpected = {
    'A': 4,
    'B': 22,
    'C': 10,
    'D1': 20,
    'D2': 36,
    'D3': 36,
    'D4': 60,
    'D5': 20,
    'D6': 24,
    'D7': 28,
    'D8': 10,
    'E': 52,
    'F': 10,
    'G': 22,
    'H': 20

}

# Create a list of the activities
activities_list = list(activitiesExpected.keys())
# Create a dictionary of the activity precedences
precedences = {
    'A': [],
    'B': [],
    'C': ['A'],
    'D1': ['A'],
    'D2': ['D1'],
    'D3': ['D1'],
    'D4': ['D2', 'D3'],
    'D5': ['D4'],
    'D6': ['D4'],
    'D7': ['D6'],
    'D8': ['D5', 'D7'],
    'E': ['B', 'C'],
    'F': ['D8', 'E'],
    'G': ['A', 'D8'],
    'H': ['F', 'G']
    }



# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in
activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in
activities_list}

# Add the constraints
for activity in activities_list:
    # Duration constraint: end time = start time + duration
    prob += end_times[activity] == start_times[activity] + activitiesExpected[activity], f"{activity}_duration"

    # Precedence constraints: start time should be after the end time of predecessors
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"
# Solve the LP problem
status = prob.solve()
# Print the results

print("Critical Path time:")
for activity in activities_list:
    print(f"{activity} starts at {value(start_times[activity])} hours and ends at {value(end_times[activity])} hours")

if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
    print(f"{activity} ends at {value(end_times[activity])} hours in duration")

"""Worst-case"""

# Create a dictionary of the activities and their durations
activitiesWorst = {
    'A': 8,
    'B': 40,
    'C': 16,
    'D1': 32,
    'D2': 48,
    'D3': 28,
    'D4': 100,
    'D5': 32,
    'D6': 40,
    'D7': 48,
    'D8': 16,
    'E': 80,
    'F': 16,
    'G': 32,
    'H': 32

}


# Create a list of the activities
activities_list = list(activitiesWorst.keys())
# Create a dictionary of the activity precedences
precedences = {
    'A': [],
    'B': [],
    'C': ['A'],
    'D1': ['A'],
    'D2': ['D1'],
    'D3': ['D1'],
    'D4': ['D2', 'D3'],
    'D5': ['D4'],
    'D6': ['D4'],
    'D7': ['D6'],
    'D8': ['D5', 'D7'],
    'E': ['B', 'C'],
    'F': ['D8', 'E'],
    'G': ['A', 'D8'],
    'H': ['F', 'G']
    }



# Create the LP problem
prob = LpProblem("Critical Path", LpMinimize)
# Create the LP variables
start_times = {activity: LpVariable(f"start_{activity}", 0, None) for activity in
activities_list}
end_times = {activity: LpVariable(f"end_{activity}", 0, None) for activity in
activities_list}

# Add the constraints
for activity in activities_list:
    # Duration constraint: end time = start time + duration
    prob += end_times[activity] == start_times[activity] + activitiesWorst[activity], f"{activity}_duration"

    # Precedence constraints: start time should be after the end time of predecessors
    for predecessor in precedences[activity]:
        prob += start_times[activity] >= end_times[predecessor], f"{activity}_predecessor_{predecessor}"
# Set the objective function
prob += lpSum([end_times[activity] for activity in activities_list]), "minimize_end_times"
# Solve the LP problem
status = prob.solve()
# Print the results

print("Critical Path time:")
for activity in activities_list:
    print(f"{activity} starts at {value(start_times[activity])} hours and ends at {value(end_times[activity])} hours")

if value(end_times[activity]) == max([value(end_times[activity]) for activity
in activities_list]):
    print(f"{activity} ends at {value(end_times[activity])} hours in duration")