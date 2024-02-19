# Animal.py
# By Logan Hedrick
# Create 2-19-24

class Animal: 
    has_brain = True
    is_alive = True
    age = 0
    name = None

    def move(speed, direction, distance):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def chirp(self):
        print("""
    /""\      ,
   <>^  L____/|
    `) /`   , /
     \ `---' /
      `'";\)`
chirp   _/_Y
""")

billy = Bird("Billy", 16)
print(f"This is {billy.name}, he is {billy.age} years old.")
billy.chirp()

ani = Animal()
print(ani.name)