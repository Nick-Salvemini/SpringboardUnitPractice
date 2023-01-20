# you have a file called score.py with the following functions
# def get_high_scores():
#     ...

# def save_high_scores():
#     ...

# and you want to export these functions to game.py
# from score import get_high_score

# high = get_high_score()

from random import randint, choice

def get_rand_year():
    return randint(1900, 2020)

def get_rand_month():    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return choice(months)