# class Eric:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health

# eric_instance = Eric("Eric the Warrior", 75)
# print(eric_instance.name)  # → Erice the Warrior
# print(eric_instance.health)  # → 75

class Creeper: 
  def __init__(self, name: str, hp: int): #constructor 
    self.name = name 
    self.hp = hp 
    
creeper1 = Creeper("explosion", 10) #Creeper() 
print(creeper1.name + " has " + str(creeper1.hp)) # → Eric