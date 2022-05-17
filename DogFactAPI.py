import requests
import json

class DogFactAPI:

  def __init__(self):
    """
    This function is setting the url as a hard coded instance variable

    Parameters:
      self: This parameter represents the current object of the class

    Returns:
      The url as an instance variable, nothing is returned in the console
    """
    self.api_url = "http://dog-api.kinduff.com/api/facts"

  def get(self):
    """
    This function requests the data from the dog fact API, turns the data into a dictionary, then returns the desired fact

    Parameters:
      self: This parameter represents the current object of the class

    Returns: 
      A fun fact about dogs
    """
    dogFact = (requests.get(self.api_url).text)
    jsonToPython = json.loads(dogFact)
    return (jsonToPython["facts"][0])

  def __str__(self):
    """
    This function creates a text string to be displayed when the program is run and a dog fact is shown

    Parameters:
      self: This parameter represents the current object of the class

    Returns:
      The string that is typed out below
    """
    return 'This is a fun fact about dogs! I had no idea, but I am glad to know now!'