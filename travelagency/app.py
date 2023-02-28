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
#    Created: 2023/02/28 09:33:30 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/28 10:00:41 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter

class TravelAgencyApp:

    _TITLE = "Agencia de Viajes"
    _GEOMETRY = "800x800+0+0"
    _MIN_SIZE = (600, 600)
    _MAX_SIZE = (800, 800)

    def __init__(self):
        self._window = tkinter.Tk()
        self._config_window()
        self._init_components()
        self._place_components()

    def _config_window(self):
        self.window.title(self._TITLE)
        self.window.geometry(self._GEOMETRY)
        self.window.maxsize(*self._MAX_SIZE)
        self.window.minsize(*self._MIN_SIZE)

    def _init_components(self):
        RADIO_BTNS = ["Monte Abantos", "La Pedriza", "Las dehesas de Cercedilla", "La Cabrera-Pico de la Miel"]
        CHK_BTNS = ["Mochila", "Linterna", "GPS", "Mapa", "Prismáticos", "Cantimplora", "Botiquín", "Crema Solar"]
        EDIT_TEXTS = ["Nombre", "Apellidos", "Dirección", "Teléfono"]
        self.rbtns = []
        self.chkbtns = []
        self.etxt = []
        # TODO

    def _place_components(self):
        pass # TODO

    def run(self) -> None:
        self.window.mainloop()

    # GETTERS
    @property
    def window(self):
        return self._window
