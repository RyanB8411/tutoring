# import random 

# NumRounds = 0
# BankPoints = 0 
# RoundPoints = 0

# print(f"Welcome to Pig it is round {NumRounds}. How many turns will it take you to win?")

# while BankPoints <100:
    
#   if RoundPoints != 0:
#     answer = input(f"\nCurrent Round: {NumRounds}\nBanked Points: {BankPoints}\nCurrent Points: {RoundPoints}\nCurrent Roll: {DiceRoll}")
        
#     if answer == "yes": 
#         BankPoints += RoundPoints
#         RoundPoints = 0 
#         NumRounds = NumRounds+1
#   elif RoundPoints == 0:
#     NumRounds += 1
        
#   DiceRoll = random.randint(1,6)
    
#   if DiceRoll == 1: 
#       RoundPoints = 0 
#       print(f"You rolled a 1 Round {NumRounds}'s points are 0.")
#       NumRounds = NumRounds+1
       
#   if 1 < DiceRoll < 7:
#       RoundPoints += DiceRoll
        

# print(f"\nCongratulation! You won on round {NumRounds}! With {BankPoints} points!")

# time = input("Is it currently day or night?:" )
# if time == 'night':
#   stars = input("Can you see the stars?: ")
#   if stars == "yes":
#     print ("Oh wow! I wonder how many there are...")
#   else:
#     print ("Oh, that's a shame, the stars are so beautiful")
# else:
#   print ("I hope the sun is shining on you!")
  
#For this example we will have a user enter a room and either go left or right but have an if or else stement to decide
in_room = True
while in_room:
  direction = input("Enter a direction")
  if direction.lower() == "left":
    print("You went left successfully")
    in_room = False
  elif direction.lower() == "right":
    print("You sucessfully went right")
    in_room = False
  else:
    print("Invalid input try again.")
#This is where we will end our session today.
#Working Today?
#