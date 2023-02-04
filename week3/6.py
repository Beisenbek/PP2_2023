class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.score = 120
  def __str__(self):
    return f"{self.name}-({self.age}:{self.score}:{self.course})"
  def setCourse(self, c):
    self.course = c


p1 = Person("John", 36)
p1.setCourse(2)
print(p1)