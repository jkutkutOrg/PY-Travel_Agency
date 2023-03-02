# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    checkbutton.py                                       ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/02 16:53:07 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from travelagency.style.style import TravelAgencyStyle as STYLE

class Checkbutton(tkinter.Checkbutton):
    def __init__(self, window, text, variable):
        super().__init__(
            window,
            text = text,
            variable = variable,
            bg = STYLE.BG,
            fg = STYLE.FG
        )
