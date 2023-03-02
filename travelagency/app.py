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
#    Updated: 2023/02/28 17:02:56 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter
import pathlib

class TravelAgencyApp:

    _TITLE = "Agencia de Viajes"
    _WIDTH = 800
    _HEIGHT = 600
    _GEOMETRY = f"{_WIDTH}x{_HEIGHT}+0+0"
    _MIN_SIZE = (_WIDTH, _HEIGHT)
    _MAX_SIZE = (_WIDTH, _HEIGHT)

    # Style
    _BG = '#333333'
    _FG = '#AAAAAA'
    _WINDOW_PADDING = 10

    def __init__(self):
        self._window = tkinter.Tk()
        self._config_window()
        self._init_components()
        # Debug
        self.w.bind("<FocusOut>", lambda e : exit())

    def _config_window(self):
        self.w.title(self._TITLE)
        self.w.config(
            #bg = self._BG
        )

        root_dir = pathlib.Path(__name__).parent.resolve()
        # TODO self.w.iconbitmap(f"{root_dir}/res/img/logo.ico")
        self._window_frame = tkinter.Frame(
            self.w,
            width = self.width,
            height = self.height,
            bg = self._BG
        )
        self._window_frame.pack_propagate(0)
        self.w.geometry(self._GEOMETRY)
        self.w.maxsize(*self._MAX_SIZE)
        self.w.minsize(*self._MIN_SIZE)
        self._window_frame.pack(
            padx = self._WINDOW_PADDING,
            pady = self._WINDOW_PADDING
        )

    def _init_components(self):
        # RADIO_BTNS = ["Monte Abantos", "La Pedriza", "Las dehesas de Cercedilla", "La Cabrera-Pico de la Miel"]
        # CHK_BTNS = ["Mochila", "Linterna", "GPS", "Mapa", "Prismáticos", "Cantimplora", "Botiquín", "Crema Solar"]
        # EDIT_TEXTS = ["Nombre", "Apellidos", "Dirección", "Teléfono"]
        # CMBBOX_OPTIONS = ["Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón"]
        self.labels = []
        self.rbtns = []
        # self.chkbtns = []
        # self.etxt = []
        # self.cmbbox = None
        # self.lstbox = None
        # self.btn_save = None
        # TODO
        self._init_title()

    def _init_title(self) -> None:
        self._title_frame = tkinter.Frame(
            self.window,
            width = self.width,
            bg = self._BG
        )
        self._title_frame.pack(
            fill = tkinter.X
        )
        # Title label
        self.labels.append(tkinter.Label(
            self._title_frame,
            text = "Viajes",
            font = ("Arial", 30),
            fg = self._FG,
            bg = self._BG
        ))
        self.labels[-1].pack(
            side = tkinter.LEFT
        )
        # Logo
        size = 100
        self._canvas = tkinter.Canvas(
            self._title_frame,
            width = size,
            height = size,
            highlightthickness=0
        )
        self._img = tkinter.PhotoImage(file="res/img/logo.png")
        self._canvas.pack(
            side = tkinter.RIGHT
        )
        self._canvas.create_image(0,0, anchor=tkinter.NW, image = self._img)


    def _init_travel_type(self) -> None:
        self.labels.append(tkinter.Label(
            self.window,
            text = "Añadir viaje:",
            font = ("Arial", 20),
            fg = self._FG,
            bg = self._BG
        ))
        self.labels[-1].pack(
            # anchor = tkinter.N,
            side = tkinter.LEFT,
            padx = 0,
            #pady = 00, # TODO img size
        )
        # rbtns_value = tkinter.StringVar()
        # self.rbtns.append(tkinter.Radiobutton(
        #     self.window,
        #     text = "Hola",
        #     variable = rbtns_value
        # ))
        # self.rbtns[-1].pack()

    def run(self) -> None:
        self.w.mainloop()

    # GETTERS
    @property
    def width(self) -> int:
        return self._WIDTH - 2 * self._WINDOW_PADDING
    
    @property
    def height(self) -> int:
        return self._HEIGHT - 2 * self._WINDOW_PADDING

    @property
    def window(self):
        return self._window_frame

    @property
    def w(self):
        return self._window
