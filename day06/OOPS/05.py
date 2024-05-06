

class Rectangle():
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def getLength(self) -> float:
        return self.length

    def setLength(self, length: float):
        self.length = length

    def getWidth(self) -> float:
        return self.width

    def setWidth(self, width: float):
        self.width = width

    def getArea(self) -> float:  # Corrected return type annotation
        return self.length * self.width

    def getPerimeter(self) -> float:  # Corrected return type annotation
        return 2 * (self.length + self.width)
    def toString(self) -> str:  # Corrected return type annotation
        return f"Rectangle: Length={self.length}, Width={self.width}, Area={self.getArea()}, Perimeter={self.getPerimeter()}"

# Example usage:
rect = Rectangle(5, 4)
print(rect.toString())
