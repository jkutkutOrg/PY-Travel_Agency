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
#    Updated: 2023/03/03 16:05:02 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

import re
from tkinter import messagebox
from travelagency.gui import TravelAgencyGUI

class TravelAgencyApp:
    def __init__(self):
        self._gui = TravelAgencyGUI()
        self._init_logic()

    def _init_logic(self) -> None:
        self._gui.btn_submit.config(command = self._submmit)

    def _submmit(self):
        traveltype = self._gui.travel_type
        if traveltype == '':
            self.error(
                "Tipo de viaje inválido.",
                "Selecciona algún viaje."
            )
            return
        items = self._gui.travel_items
        usr_data = [
            ("nombre", self._gui.travel_name, r'^[A-Za-zñÑáÁÉéíÍÓóÚú ]+$'),
            ("apellidos", self._gui.travel_surname, r'^[A-Za-zñÑáÁÉéíÍÓóÚú ]+$'),
            ("dirección", self._gui.travel_address, None),
            ("teléfono", self._gui.travel_phone, r'^(\+\d{2,3})? ?\d{3} ?(\d{3} ?\d{3}|\d{2} ?\d{2} ?\d{2})$'),
            ("población", self._gui.travel_poblacion, None),
        ]
        for key, value, regex in usr_data:
            if value == '':
                self.error(
                    f"Error en {key}",
                    f"El campo '{key}' no puede estar vacío."
                )
                return
            elif regex is not None and not re.match(regex, value):
                self.error(
                    f"Error en {key}",
                    f"El campo '{key}' no es válido."
                )
                return
        self._gui.add(
            self._format(
                traveltype,
                items,
                usr_data
            )
        )
        self._gui.reset_form()

    def _format(self, traveltype: str, items: list, usr_data: dict) -> str:
        items_str = ", ".join(items)
        name = f"{usr_data[0][1]} {usr_data[1][1]}"
        phone = usr_data[3][1]
        addr = f"{usr_data[2][1]} {usr_data[4][1]}"
        result = f"{name} - {traveltype}: {items_str} -- Datos: {phone}, {addr}"
        return result

    def run(self):
        self._gui.run()

    def error(self, title, msg) -> None:
        messagebox.showerror(title = title, message = msg)
