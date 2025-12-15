import random 
moves = ['Rock', 'Paper', 'Scissors']
user_counts = {'Rock':0, 'Paper':0, 'Scissors':0} ## To keep trck of your moves
## Initialize Scores:
player_score = 0
computer_score = 0
## Game Loop
while True:
    my_move = input("Enter your move (Rock,Paper,Scissors):").capitalize()## Get user input
    ## Validate user input, if invalid then continue the loop
    if my_move in moves:
          user_counts[my_move] += 1 ## updates user move count 
    most_common_move = max(user_counts, key=user_counts.get) ## Find the m0ost used move by user

    ## Computer selects a move that beata the user's most common move
    if most_common_move == 'Rock': 
        computer_move = 'Paper' 
    elif (most_common_move == 'Paper'):
            computer_move = 'Scissors'  
    elif  (most_common_move == 'Scissors'):
            computer_move = 'Rock'  
    else: 
            computer_move = random.choice(moves) ## Random choice for first move

    ## Determine the winner
    print("Computer's move:", computer_move)
    if my_move == computer_move:
        print("It's a tie!")
    elif(my_move == 'Rock' and computer_move == 'Scissors') or\
        (my_move == 'Paper' and computer_move =='Rock') or\
        (my_move == 'Scissors' and computer_move =='Paper'):
        print("You Win!")
        player_score += 1 ## updateplayer score
    else:
        print("Computer Wins!")
        computer_score += 1 ## update computer score
    print(f"Scores => Player: {player_score}, Computer:{computer_score}")    
   
