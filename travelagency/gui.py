# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    gui.py                                               ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/28 09:33:30 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/03/03 10:46:32 by Jkutkut            '-----------------'    #
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
from travelagency.ui.listbox import Listbox

from travelagency.style.style import TravelAgencyStyle as STYLE

class TravelAgencyGUI:

    _CHK_BTNS = ["Mochila", "Linterna", "GPS", "Mapa", "Prismáticos", "Cantimplora", "Botiquín", "Crema Solar"]

    _TITLE = "Agencia de Viajes"
    _WIDTH = 850
    _HEIGHT = 600
    _GEOMETRY = f"{_WIDTH}x{_HEIGHT}+0+0"
    _MIN_SIZE = (_WIDTH, _HEIGHT)
    _MAX_SIZE = (_WIDTH, _HEIGHT)

    def __init__(self):
        self._window = tkinter.Tk()
        self._config_window()
        self._init_components()
        # TODO Debug
        # self.w.bind("<FocusOut>", lambda e : exit())

    def _config_window(self):
        self.w.title(self._TITLE)
        self.w.config(
           bg = STYLE.BG
        )
        STYLE.initialize()
        root_dir = pathlib.Path(__name__).parent.resolve()
        # TODO self.w.iconbitmap(f"{root_dir}/res/img/logo.ico")
        self._window_frame = tkinter.Frame(
            self.w,
            width = self.width,
            height = self.height,
            bg = STYLE.BG
        )
        self._window_frame.pack_propagate(0)
        self.w.geometry(self._GEOMETRY)
        self.w.maxsize(*self._MAX_SIZE)
        self.w.minsize(*self._MIN_SIZE)
        self._window_frame.pack(
            padx = STYLE.WINDOW_PADDING,
            pady = STYLE.WINDOW_PADDING
        )

    def _init_components(self):
        self._chkbtns = []
        # TODO Rename methods: UImethods, logic...
        # TODO properties
        self._init_title()
        self._init_travel_type()
        self._init_objs()
        self._init_usr_data()
        self._init_db_ui()

    def _init_title(self) -> None:
        self._title_frame = tkinter.Frame(
            self.window,
            bg = STYLE.BG
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
            bg = STYLE.BG
        )
        self._travel_type_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
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
            bg = STYLE.BG
        )
        self._travel_types_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
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
                padx = STYLE.NORMAL_MARGIN
            )

    def _init_objs(self) -> None:
        self._obj_container = tkinter.Frame(
            self.window,
            bg = STYLE.BG
        )
        self._obj_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
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
            bg = STYLE.BG
        )
        self._objs_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        for chkbtn_label in self._CHK_BTNS:
            v = tkinter.BooleanVar()
            Checkbutton(
                self._objs_container,
                text = chkbtn_label,
                variable = v
            ).pack(
                side = tkinter.LEFT,
                padx = STYLE.NORMAL_MARGIN
            )
            self._chkbtns.append(v)

    def _init_usr_data(self) -> None:
        self._data_container = tkinter.Frame(
            self.window,
            bg = STYLE.BG
        )
        self._data_container.pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
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
            bg = STYLE.BG
        ))
        self._data_containers[-1].pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        self._txtf_name = TextField(
            self._data_containers[-1],
            hint = "Nombre"
        )
        self._txtf_name.pack(
            side = tkinter.LEFT,
            padx = STYLE.NORMAL_MARGIN
        )
        self._txtf_surname = TextField(
            self._data_containers[-1],
            hint = "Apellidos"
        )
        self._txtf_surname.pack(
            side = tkinter.LEFT,
            padx = STYLE.NORMAL_MARGIN
        )
        CMBBOX_OPTIONS = ["Madrid", "Alcobendas", "San Sebastián de los Reyes", "Algete", "Pozuelo", "Las Rozas", "Majadahonda", "Móstoles", "Alcorcón", "Boadilla del Monte", "Villaviciosa de Odón"]
        self._cmbbox_poblacion = ttk.Combobox(
            self._data_containers[-1],
            state = "readonly",
            values = CMBBOX_OPTIONS
        )
        self._cmbbox_poblacion.pack(
            side = tkinter.LEFT,
            padx = STYLE.NORMAL_MARGIN
        )
        self._cmbbox_poblacion.current(0)
        # Address and phone
        self._data_containers.append(tkinter.Frame(
            self._data_container,
            bg = STYLE.BG
        ))
        self._data_containers[-1].pack(
            fill = tkinter.X,
            pady = STYLE.NORMAL_MARGIN
        )
        self._txtf_address = TextField(
            self._data_containers[-1],
            hint = "Dirección"
        )
        self._txtf_address.pack(
            side = tkinter.LEFT,
            padx = STYLE.NORMAL_MARGIN
        )
        self._txtf_phone = TextField(
            self._data_containers[-1],
            hint = "Teléfono"
        )
        self._txtf_phone.pack(
            side = tkinter.LEFT,
            padx = STYLE.NORMAL_MARGIN
        )

    def _init_db_ui(self) -> None:
        # Btn submit
        self.btn_submit = Button(
            self.window,
            text = "Añadir viaje"
        )
        self.btn_submit.pack(
            fill = tkinter.X,
            padx = STYLE.NORMAL_MARGIN
        )
        self._lstbox = Listbox(
            self.window
        )
        self._lstbox.pack(
            fill = tkinter.BOTH,
            pady = STYLE.NORMAL_MARGIN,
            padx = STYLE.NORMAL_MARGIN
        )


    def run(self) -> None:
        self.w.mainloop()

    # GETTERS
    @property
    def width(self) -> int:
        return self._WIDTH - 2 * STYLE.WINDOW_PADDING

    @property
    def height(self) -> int:
        return self._HEIGHT - 2 * STYLE.WINDOW_PADDING

    @property
    def window(self):
        return self._window_frame

    @property
    def w(self):
        return self._window

    # Form data
    @property
    def travel_type(self) -> str:
        return self._rbtns_value.get()

    @property
    def travel_items(self) -> list:
        items = []
        for i in range(len(self._CHK_BTNS)):
            if self._chkbtns[i].get():
                items.append(self._CHK_BTNS[i])
        return items

    @property
    def travel_name(self) -> str:
        return self._txtf_name.get().strip()

    @property
    def travel_surname(self) -> str:
        return self._txtf_surname.get().strip()

    @property
    def travel_poblacion(self) -> str:
        return self._cmbbox_poblacion.get()

    @property
    def travel_address(self) -> str:
        return self._txtf_address.get().strip()

    @property
    def travel_phone(self) -> str:
        return self._txtf_phone.get().strip()

    # SETTERS
    def add(self, e: str) -> None:
        self._lstbox.insert(tkinter.END, e)

    def reset_form(self) -> None:
        # Keep the radiobtns and chkbtns to allow fast fill of another user
        self._cmbbox_poblacion.current(0)
        self._txtf_name.delete(0, tkinter.END)
        self._txtf_surname.delete(0, tkinter.END)
        self._txtf_address.delete(0, tkinter.END)
        self._txtf_phone.delete(0, tkinter.END)
