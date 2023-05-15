# Definir una clase Frame para representar un marco

class Frame:
  def __init__(self, name, slots):
    self.name = name
    self.slots = slots

  def get_slot(self, slot_name):
    return self.slots.get(slot_name, None)

  def set_slot(self, slot_name, value):
    self.slots[slot_name] = value


# Crear una ontología de pájaros

birds = []

canary = Frame("canary", {"flies": True, "lays_eggs": True})
penguin = Frame("penguin", {"flies": False, "lays_eggs": True})
ostrich = Frame("ostrich", {"flies": False, "lays_eggs": True})

birds.extend([canary, penguin, ostrich])


# Definir reglas de inferencia

def flies(x):
  if x.get_slot("flies") == True:
    return True
  elif x.get_slot("flies") == False:
    return False
  else:
    return None

def lays_eggs(x):
  if x.get_slot("lays_eggs") == True:
    return True
  elif x.get_slot("lays_eggs") == False:
    return False
  else:
    return None

def bird(x):
  for b in birds:
    if x.name == b.name:
      return True
  return False

def non_bird(x):
  for b in birds:
    if x.name == b.name:
      return False
  return True


# Ejecutar una inferencia

def infer():
  x = Frame("x", {"flies": True, "lays_eggs": True})
  
  if bird(x) and flies(x):
    print("El animal es un pájaro que vuela")
  elif non_bird(x) and not flies(x):
    print("El animal no es un pájaro y no vuela")
  else:
    print("No se puede inferir nada")
