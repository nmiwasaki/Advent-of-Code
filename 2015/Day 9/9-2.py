import re
import time

start = time.time()

f = open("2015/Day 9/input.txt")
filecontents = f.readlines()
f.close()

# Gather a list of locations
locations = list()
pattern = r"([A-Za-z]+) to ([A-Za-z]+) = (\d+)"
for line in filecontents:
    match = re.match(pattern, line)
    for i in range(2):
        if match.groups()[i] not in locations:
            locations.append(match.groups()[i])

# Create a list of possible routes
routes = [[locations[0]]]       # include first location
for i in range(1, len(locations)):
    new_routes = []
    for j in routes:
        for k in range(len(j) + 1):
            new_route = j.copy()
            new_route.insert(k, locations[i])
            new_routes.append(new_route)
    routes = new_routes

# Test every route
longest_route = None
longest_distance = float("-inf")
for route in routes:
    total_distance = 0
    for i in range(len(route) - 1):
        location1 = route[i]
        location2 = route[i + 1]
        for line in filecontents:
            match = re.match(pattern, line)
            name1 = match.groups()[0]
            name2 = match.groups()[1]
            if match.groups()[0] == location1 and match.groups()[1] == location2 or match.groups()[0] == location2 and match.groups()[1] == location1:
                total_distance += int(match.groups()[2])
                break
    if total_distance > longest_distance:
        longest_distance = total_distance
        longest_route = route.copy()

stop = time.time()
print(f"The longest possible distance is {longest_distance} using the route {longest_route}\nThis calculation required {(stop - start):.3} seconds")