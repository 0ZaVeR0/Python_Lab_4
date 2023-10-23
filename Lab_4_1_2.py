from cube import Cube
from pyramid import Pyramid

print("Create cube(2): ")
c = Cube(2)
print("Cube: ", c)
print("volume: ",c.volume(), "\n")

print("Create cube(4): ")
c1 = Cube(4)
print("Cube: ", c1, "\n")

c3 = c1 * c
print("Mult of 2 cubes >> ",c3, "\n")


print("Create pyramid(1,2,1): ")
p = Pyramid(1,2,1)
print("Pyramid: ", p)
print("volume: ",p.volume(), "\n")

print("Create same cube(4): ")
c2 = Cube(4)
print("Cube: ", c2)