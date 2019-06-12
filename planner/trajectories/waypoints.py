import math


def scatter():
    return [[10.0, 0.0, 3.0], [10.0, 10.0, 3.0], [0.0, 10.0, 3.0], [0.0, 0.0, 3.0]]


def circle(sides, radius, altitude):
    waypoints = [[0, 0, altitude]]
    x = 0.0
    angle = 360 / sides
    for i in range(sides+1):
        x = x + math.cos(i * angle * 3.14 / 180) * radius
        y = -x + math.sin(i * angle * 3.14 / 180) * radius
        waypoints.append([float(round(x)), float(round(y)), altitude])
    waypoints.append([0, 0, altitude])
    print("waypoints:")
    print(waypoints)
    return waypoints
