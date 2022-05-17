import random
from DogFactAPI import DogFactAPI
from CatFactAPI import CatFactAPI

def userActionFunction():
  """
  This function randomizes which animal the fact displayed will be about, and displays the fun fact as well as the string created in the respective class

  Paramters:
    No parameters

  Returns:
    Either a dog or cat fact and a comment following the fact displayed
  """
  x = int(random.randrange(0,2))
  dog = DogFactAPI()
  cat = CatFactAPI()
  if x == 1:
    print(dog.get())
    print(dog)
  if x == 0:
    print(cat.get())
    print(cat)
  

