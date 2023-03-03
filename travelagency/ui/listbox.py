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
#    Updated: 2023/03/03 11:31:33 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

from travelagency.style.style import TravelAgencyStyle as STYLE

class Listbox(tkinter.Listbox):
    def __init__(self, window):
        self.container = tkinter.Frame(
            window,
        )
        super().__init__(
            self.container,
            bg = STYLE.LST_BG
        )
        scrolly = tkinter.Scrollbar(
            self.container,
            orient = tkinter.VERTICAL
        )
        scrolly.pack(
            side = tkinter.RIGHT,
            fill = tkinter.Y
        )
        self.config(yscrollcommand = scrolly.set)
        scrolly.config(command = self.yview)
        scrollx = tkinter.Scrollbar(
            self.container,
            orient = tkinter.HORIZONTAL
        )
        scrollx.pack(
            side = tkinter.BOTTOM,
            fill = tkinter.X
        )
        self.config(xscrollcommand = scrollx.set)
        scrollx.config(command = self.xview)

    def pack(self, fill, padx, pady) -> None:
        self.container.pack(fill = fill, padx = padx, pady = pady)
        super().pack(
            fill = tkinter.X
        )
