def distance_fallen(time: float):
    """Gives the distance in meters an object in freefall has fallen after time seconds"""
    return time * time * 9.8 * 0.5
dist = distance_fallen(1)
print (dist)