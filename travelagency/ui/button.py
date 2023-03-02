# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    button.py                                            ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/02 14:15:52 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from travelagency.style.style import TravelAgencyStyle as STYLE

class Button(tkinter.Button):
    def __init__(self, window, text):
        super().__init__(
            window,
            text = text,
            highlightbackground = STYLE.BG, # TODO fix
            highlightcolor = STYLE.FG,
        )