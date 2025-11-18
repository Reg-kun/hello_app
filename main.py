# from dotenv import load_dotenv
# import os 

# load_dotenv()
# my_variable = os.getenv('MY_KEY')

# print(my_variable)

# def main():
#     print("Hello from hello!")

# name = "Tom"

# if __name__ == "__main__":
#     main()




# class cat:
  
#    def  __init__(self, name, color):
#      self.name = name
#      self.color = color
#    def run(self):
#      print(f"{self.color}Кот бежит")
     
# cat1 = cat(name= "Дартаньян", color= "green")
# cat2 = cat(name= "Демогаргон", color= "grey")

# cat1.tail = "у Дартаньяна есть хвост"
# cat2.tail = "у Демогаргона нету хвоста"
# cat1.run()


# print(cat1.name, cat1.color, cat1.tail)
# print(cat2.name, cat2.color, cat2.tail)


# class nps:
#   name = "Житель"
#   body_color = "Смуглый"
#   hp = 50
  
#   def __init__(self,name,body_color,hp):
#     self.name = name
#     self.body_color = body_color
#     self.hp = hp
#   def get_damage(self,damage):
#     self.hp -= damage
#     print("вы получили 12 урона")
#   def regenerate(self,regenerate):
#     self.hp += regenerate
#     print("Вы восполнили 5 здоровьи")
    
# gitel_nps = nps(name="Житель", body_color="Смуглый", hp=50)
# gitel_nps.get_damage(12)
# print(gitel_nps.hp)

# gitel_nps.regenerate(5)
# print(gitel_nps.hp)


# class nps:
#   name = "Демогаргон"
#   color =  "Серый"
#   hp = 350
  
#   def __init__(self, name, color, hp):
#     self.name = name
#     self.color = color
#     self.hp = hp
    
#   def get_damage(self, damage):
#     self.hp -= damage
#     print("Вуил Примудрый атаковал Демогаргона, он получил 150 урона")
    
#   def get_regen(self, regen):
#     self.hp += regen
#     print("Демогаргон решил перекусить, он восстановил 95 здоровьи")
    
# demogorgon_nps = nps(name="Демогаргон", color="Серый", hp=350)
# demogorgon_nps.get_damage(150)
# print(demogorgon_nps.hp)

# demogorgon_nps.get_regen(95)
# print(demogorgon_nps.hp)

class Person:
  
    def __init__(self, name, age):
      self.__user_name = name       # __name имя старновится приватным и никто его не изменит
      self.__user_age = age
      
    def print_person(self):
        print(f"Имя: {self.__user_name}, Возраст: {self.__user_age}")
      
    @property  
    def age(self):
      return self.__user_age   
    
    @age.setter
    def age(self, age):
      if 0 < age and age < 100:
        self.__user_age = age
      else:
        print("Недопустимый возраст") 
        
person_tom = Person("Tom", 30)

person_tom.age = 19
print(person_tom.age)

# def main():
#   print("Hello from hello!")
  
  
# if __name__ == "__main__":
#   main()