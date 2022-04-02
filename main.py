import requests
import random
import time
import os

ord = ["1","2","3","4","5","6","7","8","9","0"]

start = input('How many games do you want to find?: \n')

lastupdate = 0
checked = 0
currentlyfound = 0

listofcodes = []

def saveToFile():
  list = ''
  for value in listofcodes:
    list = f"{list}{value}"
  foundgames = open("foundgames.txt","w")
  foundgames.write(list)

def reset():
  os.system("clear")
  os.system("python main.py")

def doGameExist(pin):
  url = 'https://kahoot.it/reserve/session/' + pin + '/?1648911319148'
  resposne = requests.get(url)
  global lastupdate,checked,currentlyfound
  lastupdate+=1
  checked+=1
  if lastupdate == 50:
    print(f"New update, checked: {checked}")
    lastupdate = 0
  if resposne.status_code == 200:
    print(f"Found game! - {pin}")
    currentlyfound+=1

    listofcodes.append(pin + "\n")

if start.isnumeric():
  if int(start) <= 1000:
    for lp in range(int(start)):
      pin = ''
      for lp in range(7):
        pin = pin + random.choice(ord)
      doGameExist(pin)
    print(f"Done checking {start} games!")
    whatDoYouWant = input("Save all codes in foundgames.txt? (S)\nRead all codes? (R)\nReset and begin again? (E)\n> ")
    if whatDoYouWant == "S" or whatDoYouWant == "s":
      print(f"Saved {currentlyfound} codes in foundgames.txt")
      saveToFile()
      time.sleep(1)
      reset()
    elif whatDoYouWant == "R" or whatDoYouWant == "r":
      if currentlyfound != 0:
        print("Here are all the codes")
        for values in listofcodes:
          print(values)
        beginAgain = input('Type R to reset and begin again \n> ')
        if beginAgain == 'R' or beginAgain == 'r':
          reset()
    elif whatDoYouWant == "E" or whatDoYouWant == "e":
      reset()