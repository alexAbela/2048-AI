from cmath import sqrt
from scipy import rand
from board import Board
import numpy as np
import math
import random
import copy

valid_moves = ['w', 'a', 's', 'd'] # WASD controls

def start_game():
    board = Board()
    board.add_new_num()
    board.print_state()
    while(True):
        x = input()
        if x == 'q':
            break

        """ Check if board is full"""
        if (board.is_full()):
            print("Game over")
            print("final score: " + str(board.calculateScore())) 
            return
        
        """begin State evaluation of 4 moves. Playing between 25-50 games in each random state"""
        if x == 'i':
            stateEvaluation = {'w': '', 'a': '', 's': '', 'd': ''}
            while not board.is_full():
                for move in valid_moves:
                    totalReward = 0
                    randomGames = random.randint(5,25)
                    """play random amount of random games """
                    for i in range(randomGames):
                        copyBoard = copy.deepcopy(board)
                        totalReward += playRandomGame(copyBoard, move)
                        # I may have misunderstood forula as sqrt number is always 0
                    UCB = (totalReward/randomGames) + sqrt(((2*np.log(1)))/randomGames) 
                    stateEvaluation[move] = UCB.real
                print(stateEvaluation)
                optimalMove = max(stateEvaluation, key = lambda k: stateEvaluation[k])
                print(optimalMove)
                doMove(board, optimalMove, True)
        if (x in valid_moves):
           doMove(board, x, True)
        else:
            print('Not a valid move')
    
    print('Finished')

def doMove(board, x, showMoves):
    """ If shuffle returns true, then it means that the board has changed and we can add a new number"""
    if (board.shuffle(x)):
        board.add_new_num()
         
        if(showMoves):           
            board.print_state()
            print(x + " - Current Score:" + str(board.calculateScore()))
        """Calculate and print score for the current round"""
        #totalScore = board.calculateScore()
        #print('Score: ' + str(totalScore))

"""play game with random moves"""
def playRandomGame(board, firstMove):
    if not doMove(board, firstMove, False):
        return 0
    while not board.is_full():
        doMove(board, valid_moves[random.randint(0,3)], False)
    ##print("Final Score: " + str(board.calculateScore()))
    return board.calculateScore()


start_game()