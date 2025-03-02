from dataclasses import dataclass
import doctest
import math


@dataclass
class Vector:
    x: float
    y: float

    def __repr__(self):
        """Return string representation of Vector.

        Returns:
            str: String representation in format 'Vector(x, y)'

        Examples:
            >>> v = Vector(1, 2)
            >>> repr(v)
            'Vector(1, 2)'
            >>> v = Vector(-3.5, 0)
            >>> repr(v) 
            'Vector(-3.5, 0)'
        """
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        """Calculate the magnitude (length) of the vector using Pythagorean theorem.

        Returns:
            float: The magnitude of the vector

        Examples:
            >>> v = Vector(3, 4)
            >>> abs(v)
            5.0
            >>> v = Vector(-2, -2)
            >>> abs(v)
            2.8284271247461903
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """Convert vector to boolean based on magnitude.

        Returns:
            bool: True if vector has non-zero magnitude, False otherwise

        Examples:
            >>> v = Vector(3, 4)
            >>> bool(v)
            True
            >>> v = Vector(0, 0)
            >>> bool(v)
            False
        """
        return bool(abs(self))

    def __add__(self, other):
        """Add two vectors.

        Args:
            other (Vector): Vector to be added

        Returns:
            Vector: Sum of the two vectors

        Examples:
            >>> v1 = Vector(2, 4)
            >>> v2 = Vector(-1, 2) 
            >>> v1 + v2
            Vector(1, 6)
            >>> v = Vector(3, 4)
            >>> v + v
            Vector(6, 8)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """Multiply vector by a scalar.

        Args:
            scalar (int, float): Number to multiply vector components by

        Returns:
            Vector: New vector with components multiplied by scalar

        Examples:
            >>> v = Vector(3, 4)
            >>> v * 3
            Vector(9, 12)
            >>> v * -2
            Vector(-6, -8)
            >>> v * 0
            Vector(0, 0)
        """
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    doctest.testmod()
