import math

class Point:
    def __init__(self, x=0, y=0):
        """Initialize the point with coordinates x and y."""
        self.x = x
        self.y = y

    def set_location(self, x, y):
        """Set the location of the point."""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Calculate the distance from the origin (0, 0)."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other_point):
        """Calculate the distance from another point."""
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Example usage
point1 = Point()
point1.set_location(3, 4)
print("Distance from origin:", point1.distance_from_origin())

point2 = Point(6, 8)
print("Distance from point1 to point2:", point1.distance(point2))

# Alternative way to call methods using the class name
Point.set_location(point1, 3, 4)
print("Distance from origin (alternative call):", Point.distance_from_origin(point1))
print("Distance from point1 to point2 (alternative call):", Point.distance(point1, point2))

print('\n--- Oleh L200234275 ---')