class person:
   def __init__(self,name,age):
    self.name=name
    self.age=age
   def info(self):
    print(f"I am {self.name}.I am {self.age} years old.")
    return "That's all "

class doctor(person):
  def __init__(self,name,age,doctor):
    self.name=name
    self.age=age
    self.prof=doctor
  def info(self):
    #super().info()
    print(f"I am {self.name}.I am {self.age} years old. I am currently {self.prof}.")
    return "That's all "

class surgeon(person):
  def __init__(self,name,age,surgeon):
    self.name=name
    self.age=age
    self.prof=surgeon
  def info(self):
    #super().info()
    print(f"I am {self.name}.I am {self.age} years old. I am currently {self.prof}.")
    return "That's all "

class Family_doctor(doctor,surgeon):
  def __init__(self,name,age,Family_doctor):
    self.name=name
    self.age=age
    self.prof=Family_doctor
  def info(self):
    super().info()
    print(f"I am {self.name}.I am {self.age} years old. I am currently your {self.prof}.")
    return "That's all "

ob = person("A",23)
a = doctor("Chitranshi",25,"Doctor")
b = surgeon("Mitashi",22,"Surgeon")
c = Family_doctor("Dhruvi",30,"Family_doctor")

print(ob.info())
print(a.info())
print(c.info())
