"""
Name:video_game.py
Author: Ansonia McIntire
Date: October 16, 2024
Purpose: 
"""

class Video_Game_Store:

    def __init__(self, _title, _price):

        # _title
        self._title = _title

        # _price
        self._price = _price

        

    # display_game()
    def display_game(self):
        
        print(f"The game is {self._title} and the price is {self._price}\n")

       
        

MineCraft = Video_Game_Store("MineCraft", 19.99)
MineCraft.display_game()

Genshin_Impact = Video_Game_Store("Genshin Impact", 25.47)
Genshin_Impact.display_game()

League_of_Legends = Video_Game_Store("League of Legends", 30.99)
League_of_Legends.display_game()

