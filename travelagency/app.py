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
#    Updated: 2023/03/02 14:54:15 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import tkinter
from tkinter import ttk
import pathlib

from travelagency.ui.textfield import TextField
from travelagency.ui.label import TitleLabel, SubTitleLabel
from travelagency.ui.radiobutton import Radiobutton
from travelagency.ui.checkbutton import Checkbutton
from travelagency.ui.button import Button

class TravelAgencyApp:

    _TITLE = "Agencia de Viajes"
    _WIDTH = 850
    _HEIGHT = 600
    _GEOMETRY = f"{_WIDTH}x{_HEIGHT}+0+0"
    _MIN_SIZE = (_WIDTH, _HEIGHT)
    _MAX_SIZE = (_WIDTH, _HEIGHT)

    # TODO remove Style
    _BG = '#333333'
    _FG = '#AAAAAA'
    _WINDOW_PADDING = 10
    _NORMAL_MARGIN = 10

    def __init__(self):
        self._window = tkinter.Tk()
        self._config_window()
        self._init_components()
        # TODO Debug
        self.w.bind("<FocusOut>", lambda e : exit())

    def _config_window(self):
        self.w.title(self._TITLE)
        self.w.config(
           bg = self._BG
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
        self.rbtns = []
        self.chkbtns = []
        # self.etxt = [] # TODO use
        # self.cmbbox = None # TODO add
        self.btn_submit = None
        self.lstbox = None
        # TODO Refactor containers
        # TODO Refactor style
        # TODO Rename methods: UImethods, logic...
        # TODO properties
        # TODO UI class and logic class
        self._init_title()
        self._init_travel_type()
        self._init_objs()
        self._init_usr_data()
        self._init_db_ui()

    def _init_title(self) -> None:
        self._title_frame = tkinter.Frame(
            self.window,
            bg = self._BG
        )
        self._title_frame.pack(
            fill = tkinter.X
        )
        # Title label
        TitleLabel(
            self._title_frame,
            "Viajes"
        ).pack(
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
        SubTitleLabel(
            self._travel_type_container,
            text = "Añadir viaje:"
        ).pack(
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
            Radiobutton(
                self._travel_types_container,
                text = rbtn_label,
                value = rbtn_label,
                variable = self._rbtns_value
            ).pack(
                side = tkinter.LEFT,
                padx = self._NORMAL_MARGIN
            )

    def _init_objs(self) -> None:
        self._obj_container = tkinter.Frame(
            self.window,
            bg = self._BG
        )
        self._obj_container.pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        # Section label
        SubTitleLabel(
            self._obj_container,
            text = "Accesorios:"
        ).pack(
            anchor = tkinter.NW
        )
        # Types
        self._objs_container = tkinter.Frame(
            self._obj_container,
            bg = self._BG
        )
        self._objs_container.pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        CHK_BTNS = ["Mochila", "Linterna", "GPS", "Mapa", "Prismáticos", "Cantimplora", "Botiquín", "Crema Solar"]
        for chkbtn_label in CHK_BTNS:
            v = tkinter.BooleanVar()
            e = Checkbutton(
                self._objs_container,
                text = chkbtn_label,
                variable = v
            )
            e.pack(
                side = tkinter.LEFT,
                padx = self._NORMAL_MARGIN
            )
            self.chkbtns.append({
                "v": v,
                "e": e
            })

    def _init_usr_data(self) -> None:
        self._data_container = tkinter.Frame(
            self.window,
            bg = self._BG
        )
        self._data_container.pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        # Section label
        SubTitleLabel(
            self._data_container,
            text = "Datos usuario:"
        ).pack(
            anchor = tkinter.NW
        )
        # Name, surname, población
        self._data_containers = []
        self._data_containers.append(tkinter.Frame(
            self._data_container,
            bg = self._BG
        ))
        self._data_containers[-1].pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        self._txtf_name = TextField(
            self._data_containers[-1],
            hint = "Nombre"
        )
        self._txtf_name.pack(
            side = tkinter.LEFT,
            padx = self._NORMAL_MARGIN
        )
        self._txtf_surname = TextField(
            self._data_containers[-1],
            hint = "Apellidos"
        )
        self._txtf_surname.pack(
            side = tkinter.LEFT,
            padx = self._NORMAL_MARGIN
        )
        CMBBOX_OPTIONS = ["Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón"]
        style = ttk.Style()
        style.theme_create(
            'customstyle',
            parent = 'alt',
            settings = {
                'TCombobox': {
                    'configure': {
                        'selectbackground': self._BG,
                        'fieldbackground': self._BG,
                        'background': self._BG,
                        # 'foreground': self._FG # TODO
                    }
                }
            }
        )
        style.theme_use('customstyle')
        self._cmbbox_poblacion = ttk.Combobox(
            self._data_containers[-1],
            state = "readonly",
            values = CMBBOX_OPTIONS
        )
        self._cmbbox_poblacion.pack(
            side = tkinter.LEFT,
            padx = self._NORMAL_MARGIN
        )
        # Address and phone
        self._data_containers.append(tkinter.Frame(
            self._data_container,
            bg = self._BG
        ))
        self._data_containers[-1].pack(
            fill = tkinter.X,
            pady = self._NORMAL_MARGIN
        )
        self._txtf_address = TextField(
            self._data_containers[-1],
            hint = "Dirección"
        )
        self._txtf_address.pack(
            side = tkinter.LEFT,
            padx = self._NORMAL_MARGIN
        )
        self._txtf_phone = TextField(
            self._data_containers[-1],
            hint = "Teléfono"
        )
        self._txtf_phone.pack(
            side = tkinter.LEFT,
            padx = self._NORMAL_MARGIN
        )

    def _init_db_ui(self) -> None:
        # Btn submit
        self.btn_submit = Button(
            self.window,
            text = "Añadir viaje"
        )
        self.btn_submit.pack(
            fill = tkinter.X,
            padx = self._NORMAL_MARGIN
        )
        self.lstbox = tkinter.Listbox(
            self.window,
            bg = 'grey' # TODO
        )
        self.lstbox.pack(
            fill = tkinter.BOTH,
            pady = self._NORMAL_MARGIN,
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
