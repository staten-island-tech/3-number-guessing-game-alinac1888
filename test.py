game = int(input("Guess a number between 1-10"))
while game != 8:
    game = int(input("incorrect, Guess another number between 1-10"))
    if game == 8:
      print("correct")