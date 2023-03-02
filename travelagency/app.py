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
    _NORMAL_MARGIN = 10

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
        self._init_travel_type()

    def _init_title(self) -> None:
        self._title_frame = tkinter.Frame(
            self.window,
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
        self._travel_type_container = tkinter.Frame(
            self.window,
            bg = self._BG
        )
        self._travel_type_container.pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        # Section label
        self.labels.append(tkinter.Label(
            self._travel_type_container,
            text = "Añadir viaje:",
            font = ("Arial", 20),
            fg = self._FG,
            bg = self._BG
        ))
        self.labels[-1].pack(
            anchor = tkinter.NW
        )
        # Types
        self._travel_types_container = tkinter.Frame(
            self._travel_type_container,
            bg = self._BG
        )
        self._travel_types_container.pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        self._rbtns_value = tkinter.StringVar()
        RADIO_BTNS = ["Monte Abantos", "La Pedriza", "Las dehesas de Cercedilla", "La Cabrera-Pico de la Miel"]
        for rbtn_label in RADIO_BTNS:
            self.rbtns.append(tkinter.Radiobutton(
                self._travel_types_container,
                bg = self._BG,
                fg = self._FG,
                text = rbtn_label,
                value = rbtn_label,
                variable = self._rbtns_value
            ))
            self.rbtns[-1].pack(
                side = tkinter.LEFT,
                padx = self._NORMAL_MARGIN
            )

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
