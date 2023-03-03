# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    style.py                                             ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 16:52:01 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/03 10:47:47 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter
from tkinter import ttk

class TravelAgencyStyle:
    BG = '#333333'
    LST_BG = 'grey'
    FG = '#AAAAAA'
    WINDOW_PADDING = 10
    NORMAL_MARGIN = 10

    # Text
    FONT = 'Arial'
    TITLE_TEXT_SIZE = 30
    SUBTITLE_TEXT_SIZE = 20

    @classmethod
    def initialize(cls):
        style = ttk.Style()
        style.theme_create(
            'customstyle',
            parent = 'alt',
            settings = {
                'TCombobox': {
                    'configure': {
                        'selectbackground': cls.BG,
                        'fieldbackground': cls.BG,
                        'background': cls.BG,
                        'TComboboxPopdown': {
                            'configure': {
                                'background': cls.BG,
                                'foreground': cls.FG
                            }
                        }
                    }
                }
            }
        )
        style.theme_use('customstyle')


