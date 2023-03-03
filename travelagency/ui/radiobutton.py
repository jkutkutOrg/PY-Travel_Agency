# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    radiobutton.py                                       ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/03 11:44:12 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from travelagency.style.style import TravelAgencyStyle as STYLE

class Radiobutton(tkinter.Radiobutton):
    def __init__(self, window, text, value, variable):
        super().__init__(
            window,
            text = text,
            value = value,
            variable = variable,
            bg = STYLE.BG,
            fg = STYLE.FG,
            highlightthickness = 0
        )
