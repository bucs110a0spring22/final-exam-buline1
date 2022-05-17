import requests
import json

class CatFactAPI:

  def __init__(self):
    """
    This function is setting the url as a hard coded instance variable

    Parameters:
      self: This parameter represents the current object of the class

    Returns:
      The url as an instance variable, nothing is returned in the console
    """
    self.api_url = "http://meowfacts.herokuapp.com/"

  def get(self):
    """
    This function requests the data from the cat fact API, turns the data into a dictionary, then returns the desired fact

    Parameters:
      self: This parameter represents the current object of the class

    Returns: 
      A fun fact about cats
    """
    catFact = (requests.get(self.api_url).text)
    jsonToPython = json.loads(catFact)
    return (jsonToPython["data"][0])
    

  def __str__(self):
    """
    This function creates a text string to be displayed when the program is run and a cat fact is shown

    Parameters:
      self: This parameter represents the current object of the class

    Returns:
      The string that is typed out below
    """
    return 'This is a fun fact about cats! Did you know this? I sure didnt!'