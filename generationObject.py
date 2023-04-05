import random
from firstGenerationData import objects, locations, stylings


class firstGeneration:
    def __init__(self, subject, location, styling,):
       self.subject = subject   
       self.location = location
       self.styling = styling 


    def prompt(self):
       print(f' {self.subject} in a {self.location} with {self.styling} styling ')
       

x = random.choice(objects)
y = random.choice(locations)
z = random.choice(stylings)


myObject = firstGeneration(x, y, z)

print(myObject.prompt())
