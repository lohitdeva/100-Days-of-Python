# Python script to recreate the 'Higher Lower' game by comparing Instagram followers of the top 50 most followed Instagram profiles.
#
# Created by: Lohit Deva
# 29/12/2022

import random
import os
from art import logo, vs
from game_data import data

score = 0
game_over = False
celebs = []

def celeblist(celebs):
    '''
    Accepts a list of celebrities as input\n.If the list of celebrities is empty, it adds 2 celebrities (as dictionaries) to the list.
    If the list is already populated, it swaps positions between the first and second celebrity and also replaces the second celebrity with a new one.
    It also carries a check to make sure that new celebrity is not currently in the list or an immediate predecessor,\ni. e,
    celeb 'a' is removed, celeb 'b' -> celeb 'a', and new celeb 'b' is neither old celeb 'a' nor new celeb 'a'.
    '''
    if celebs == []:
        celebs = random.sample(data, 2)
    else:
        _ = celebs[0]
        celebs[0] = celebs[1]
        # random.sample returns a list. Thus the indexing [0] is required
        celebs[1] = random.sample(data, 1)[0]
        while celebs[1] == _ and celebs[1] == celebs[0]:
            celebs[1] = random.sample(data, 1)[0]
    return celebs

def celebinfo(celeb):
    '''
    Accepts a celebrity as a dictionary.\nReturns the name, description and country of the celebrity in a formatted string.
    '''
    return f"{celeb['name']}, a {celeb['description']}, from {celeb['country']}"

def dispcelebs(celeb1, celeb2):
    '''
    Accepts two celebrities as dictionaries and displays their information.
    '''
    print(f"Compare A:\n{celebinfo(celeb1)}")
    print(vs)
    print(f"Compare B: \n{celebinfo(celeb2)}")
    
def makechoice(celeb1, celeb2):
    '''
    Accepts two celebrities as dictionaries.\nUser is asked to enter their choice
    which is then validated and returned as True or False.
    '''
    correct_choice = 'a' if celeb1['follower_count'] >= celeb2['follower_count'] else 'b'
    choice = input("Who has more followers? Type 'a' or 'b'\n").strip().lower()
    while choice != 'a' and choice != 'b':
        choice = input("That was an invalid choice, please try again. Type 'a' or 'b'\n")
    return True if choice == correct_choice else False

def game(score, game_over, celebs):
    '''
    Begins the game 'Higher Lower' where the objective of the user is to guess which among the two celebrity
    profiles has a higher follower count.\nThe game goes on until the user enters the wrong choice and the score
    is continuously displayed on the screen, incrementing for every correct answer.
    '''
    while True:
        os.system('cls')
        print(logo)
        
        if not game_over:
            celebs = celeblist(celebs)
               
            if score != 0:
                print(f"You're right! Current score {score}")
                
            dispcelebs(celebs[0], celebs[1])
        
            if makechoice(celebs[0], celebs[1]):
                score += 1
            else:
                game_over = True
                
        else:
            print(f"Sorry, that was wrong. Final score: {score}")
            break
    

game(score, game_over, celebs)