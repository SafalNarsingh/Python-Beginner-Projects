# Game of dice 
'''
    No. of players 2 - 4
    Dice numbers from 1 to 6
    
    Basic Rules:
        1. There will be three rounds
        2. Each player will have their turn to roll the dice
        3. The current player will role the dice
        4. The system will ask the player for further roll
            If yes, then the dice rolls and adds the score 
            and if the dice is 1 then the turn is over and score becomes 0
            If no, then for this round the turn for the player is over and has to wait for another round
        5. Total score of each player is counted and then the highest score wins

    Have Fun!!!
'''
import random

#function 4
def output(highest_score,player_name):
    '''This function accepts the index of highest score along with all players name
        The criteria for draw is set to -1.
        So if highest_scorer index is -1 then draw is printed
        else the name along with congratulation is printed 
      
        output(int,list) -> prints result
    '''
    if(highest_score == -1):
        print("Awesome Match! The game ended with a tie.")
        print("OOf.Try Again?")       
    else:
        print(player_name[highest_score],'won the game!')
        print('Congratulations')
    print('------------------------------------------\n')


#function 3
def winner_finder(players_score,players_no):
    '''
     This is the third function used in this code.
     Here, the highest scorer index is found using a simple logic
     if the score of any players are same then the variable count is increased
     if count is equal to no.of players-1 then it means the game resulted in a draw so -1 is returned to the calling function
     else the highest scorer index is returned
    '''
    highest_score = 0
    count = 0

    for i in range(1,players_no):
        if(players_score[highest_score]==players_score[i]):
            count += 1
        elif(players_score[highest_score]<players_score[i]):
            highest_score = i

    if(count == players_no-1):
        return -1
    else:
        return highest_score

#function 2
def roll_checker(check):
    #This functions checks if the input roll is valid or not
    '''
        this function runs a loop until the player enters a valid response to the question and correspoding output is sent
        1 for y/Y
        0 for n/N

    '''
    while(check not in ['y','Y','n','N']):
            print("Input valid decision!!!")
            print("Either y or n")
            check = input('Do you want to roll(y/n): ')

    if(check in ['y','Y']):
        return 1
    elif(check in ['n','N']):
        return 0


#function 1
def game(players_no): #execution module for the game
    ''' The whole game will be executed within this function and the results will be sent to the main module
        name of players is accepted and stored
        the dice is rolled in this section 
        where the total score is also calculated 
        function 2,3 and 4 are called in this program 
    '''
    print('------------------------------------------\n')
    i = 0
    players_score = [None] * players_no
    player_name = [None] * players_no
    score = 0
    for i in range(0,players_no):
        player_name[i] = input("Enter player "+str(i+1)+"\'s name: ")


    for i in range(0,players_no):
        print('------------------------------------------\n')
        score = 0
        print("Player ",i+1,"'s turn:")

        check = (input("Do you want to roll?(y/n): "))
        roll = roll_checker(check) #calling function 2 and storing its returned value
        while(roll == 1):


            print('\n')
            dice_score = random.randint(1,6)
            print('You rolled a ',dice_score)
            score = score + dice_score
            print('Total Score: ',score)

            check = (input("Do you want to roll?(y/n): "))
            roll = roll_checker(check) #calling function 2 and storing its returned value

            if(dice_score == 1):
                print('Congrats! You got 1!')
                print('Your score became 0')
                score = 0
                print('Turn Over.')
                break

        print('------------------------------------------\n')
        print('Player',str(i+1)+'\'s Total Score: ',score)    
        print('------------------------------------------\n')
        
        players_score[i] = score
    
    print('Scoreboard: ')
    for i in range(0,players_no):
         print('Player',str(i+1)+'.',player_name[i]+'\'s Total Score: ',players_score[i])    


    print('------------------------------------------\n')
    highest_score = winner_finder(players_score,players_no) #calling function 3 and storing its returned value
    output(highest_score,player_name) #calling function 4

           

#main program
print('------------------------------------------\n')

players_no = input('Enter the numbers of player: ')
print('------------------------------------------\n')

if(players_no.isdigit() == True):

    players_no = int(players_no)
    if(players_no <2 or players_no>4):

        print("Please enter number between 2 and 4!")
        while(players_no <2 or players_no>4):
            players_no = int(input('Enter the numbers of player: '))


    game(players_no) #calling the main module function for the game
    
   

else:
    print("Invalid Input!")
    print("Please restart the game!")
    print('------------------------------------------\n')





