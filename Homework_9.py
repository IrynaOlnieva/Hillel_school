# Write Abstract class Figure
# Inherit Triangle and Round from it
#  Create a collection of Figures, count perimeter and square of them

from abc import ABC, abstractmethod
import math
class Figure(ABC):
     def __init__(self, first_side,second_side,third_side):
         self.first_side = first_side
         self.second_side = second_side
         self.third_side = third_side


     @abstractmethod
     def get_perimetr(self):
         pass

     @abstractmethod
     def get_square(self):
         pass

class Triangle(Figure):
     def __init__(self, first_side,second_side,third_side,height):
         super().__init__(first_side,second_side,third_side)
         self.height = height

     def get_perimetr(self):
        return  self.first_side + self.second_side + self.third_side

     def get_square(self):
        return (self.first_side * self.height)/2



class Round(Figure):
    def __init__ (self, radius):
        self.radius = radius

    def get_perimetr(self):
        return 2 * math.pi * self.radius

    def get_square(self):
        return math.pi * self.radius ** 2



Triangle = Triangle(first_side = 5,second_side = 7,third_side = 8,height = 10)
Triangle.get_perimetr()
Triangle.get_square()
print(f"Perimetr triangle: {Triangle.get_perimetr()}")
print(f"Square triagle: {Triangle.get_square()}")

Round = Round(radius=50)
Round.get_perimetr()
Round.get_square()
print(f"Perimetr round: {Round.get_perimetr()}")
print(f"Square round: {Round.get_square()}")