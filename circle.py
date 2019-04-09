from math import pi


class Circle:
    def __init__(self, radius: float = 1) -> None:
        self._radius = radius

    def __repr__(self) -> str:
        return f"Circle({self.radius})"

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, radius) -> None:
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def diameter(self) -> float:
        return 2 * self.radius

    @diameter.setter
    def diameter(self, diameter) -> None:
        self.radius = diameter / 2

    @property
    def area(self) -> float:
        return pi * self.radius * self.radius
