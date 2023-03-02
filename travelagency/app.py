# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    app.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/03/02 16:56:06 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/02 17:01:25 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

from travelagency.gui import TravelAgencyGUI

class TravelAgencyApp:
    def __init__(self):
        self._gui = TravelAgencyGUI()

    def run(self):
        self._gui.run()
