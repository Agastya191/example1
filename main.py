print("welcome to murder island your goal is to kill the king and bring back order to the land")
print("face the obstacles to win")
print("Write your answer with no caps for all answers:")
left_or_right=input("do you want to go left or right: ")
print(left_or_right)
if left_or_right=="left":
  print("you make it to a dungen")
else:
  print("some solders find you and gun you down")

question=input("will you ask anyone for directions:")
if question=="yes":
  print(" the people look at you weird but they tell you to head to the lake")
else:
  print("you wander around and get locked in the dungen for looking SUS")

house=input("you head to the lake but there is a house will you go inside it:")
if house=="yes":
  print("you head into the house and there are 3 doors red, yellow, blue")
else:
  print("you go to the back of the house and a soldier finds and kills you ")
door=input("which door will you pick:")
if door== "red":
  print("it's a room full of explosives ")
elif door=="yellow":
  print("you open the door and the king of the land pops out")
elif door=="blue":
  print("you open the door and water splashes out you swim your way to the end and come face to face with a megaladon")
print("(king)I see that you have gotten past all the lines of defense so what do you want")
choice=input("there is a sword next to you do you pick it up or not:")
if choice=="yes":
  print("you pick it up and 2 soldiers pop out you dodge both of their attacks and kill them both")
  print("(king) wow i did not expect that. Please don't kill me ")
  print("(you) your the reason this place is corrupt either step down or i kill you.")
  print("(king) NEVER")
  print("(you) then die")
  print("YOU WIN")
else:
  print("2 soldiers pop out and kill you")
