# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.



# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.


# Bonus Challenge (Optional)
# If you want an extra challenge:

# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!


# 💡 Tip:

# Test your implementation by creating several circles and printing comparisons, additions, and sorted results.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    @property
    def diameter(self):
        return self.radius * 2
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area()})"
    def __repr__(self):
        return f"Circle({self.radius})"
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __gt__(self, other):
        return self.radius > other.radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    

c1 = Circle(5)
c2 = Circle(3)
c3 = Circle(8)
c4 = Circle(3)

c5 = Circle.from_diameter(10)

print("=== display (__str__) ===")
print(c1)
print(c2)
print(c5)

print("\n=== Area ===")
print(f"Area of c1 (r=5) : {c1.area()}")
print(f"Area of c3 (r=8) : {c3.area()}")

print("\n=== Addition (__add__) ===")
c6 = c1 + c2
print(f"c1 (r=5) + c2 (r=3) = {c6}")

print("\n=== Comparison (__gt__, __eq__) ===")
print(f"c1 (r=5) > c2 (r=3) : {c1 > c2}")
print(f"c1 (r=5) == c2 (r=3) : {c1 == c2}")
print(f"c2 (r=3) == c4 (r=3) : {c2 == c4}")

print("\n=== Equality (__eq__) ===")
print(f"c2 (r=3) == c4 (r=3) : {c2 == c4}")
print(f"c1 (r=5) == c3 (r=8) : {c1 == c3}")

print("\n=== Sorting a list of circles (__lt__) ===")
circles = [c1, c2, c3, c4]
sorted_circles = sorted(circles)
print(sorted_circles)