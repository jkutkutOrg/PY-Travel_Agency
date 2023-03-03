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
#    Updated: 2023/03/03 09:46:26 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

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
            print("Invalid traveltype")
            return
        items = self._gui.travel_items
        usr_data = [
            ("nombre", self._gui.travel_name, None),
            ("apellidos", self._gui.travel_surname, None),
            ("dirección", self._gui.travel_address, None),
            ("teléfono", self._gui.travel_phone, None),
            ("población", self._gui.travel_poblacion, None),
        ]
        for key, value, regex in usr_data:
            if value == '':
                print(f"Invalid {key}")
                return
            elif regex is not None and not regex.match(value):
                print(f"Invalid regex of {key}")
                return
        self._gui.add(
            self._format(
                traveltype,
                items,
                usr_data
            )
        )
        # self._gui.reset_form()

    def _format(self, traveltype: str, items: list, usr_data: dict) -> str:
        print(traveltype)
        items_str = ", ".join(items)
        print(items_str)
        print(usr_data)
        name = f"{usr_data[0][1]} {usr_data[1][1]}"
        result = f"{name} - {traveltype}: {items_str}"

        return result

    def run(self):
        self._gui.run()
