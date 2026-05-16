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
    
  def show_stats(self):
    print(self.name + " has " + str(self.hp)) # → Eric


creeper1 = Creeper("explosion", 10) #Creeper() 
creeper1.show_stats() # → explosion has 10 hp
creeper2 = Creeper("silicon volcano", 20)
creeper2.show_stats() # → silicon volcano has 20 hp

# print(creeper1.name + " has " + str(creeper1.hp)) # → Eric