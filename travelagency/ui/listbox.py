# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    listbox.py                                           ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 14:11:45 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/03 11:06:23 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from travelagency.style.style import TravelAgencyStyle as STYLE

class Listbox(tkinter.Listbox):
    def __init__(self, window):
        super().__init__(
            window,
            bg = STYLE.LST_BG
        )
        scrolly = tkinter.Scrollbar(window)
        scrolly.pack(
            side = tkinter.RIGHT,
            fill = tkinter.Y
        )
        self.config(yscrollcommand = scrolly.set)
        scrolly.config(command = self.yview)

        scrollx = tkinter.Scrollbar(
            window,
            orient = tkinter.HORIZONTAL
        )
        scrollx.pack(
            side = tkinter.BOTTOM,
            fill = tkinter.X
        )
        self.config(xscrollcommand = scrollx.set)
        scrollx.config(command = self.xview)
