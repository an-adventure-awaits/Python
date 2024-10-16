"""
Name:video_game.py
Author: Ansonia McIntire
Date: October 16, 2024
Purpose: 
"""

class video_game:

    def __init__(self, _title, _price, _game_name_1, _game_name_2, _game_name_3):

        # _title
        self._title = _title

        # _price
        self._price = _price

        # game_name_1
        self._game_name_1 = _game_name_1
        _game_name_1 = "Minecraft"
        self._game_name_cost_1 = 19.99

        # game_name_2
        self._game_name_2 = _game_name_2
        _game_name_2 = "Genshin Impact"
        self._game_name_cost_2 = 25.47

        # game_name_3
        self._game_name_3 = _game_name_3
        _game_name_3 = "League of Legends"
        self._game_name_cost_3 = 30.99

        

    # display_game()
    def display_game(self):
        
        print(f"The first game is {self._game_name_1} for ${self.game_name_cost_1}\n")

        print(f"The seccond game is {self._game_name_2} for ${self.game_name_cost_2}\n")

        print(f"The third game is {self._game_name_3} for ${self.game_name_cost_2}")

