import tkinter
from tkinter import ttk

class TextField(tkinter.Entry):
    def __init__(self, window, hint, hint_color='grey'):
        super().__init__(window)

        self.hint = hint
        self.hint_color = hint_color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self._put_hint()

    def _put_hint(self):
        self.insert(0, self.hint)
        self['fg'] = self.hint_color

    def foc_in(self, *args):
        if self['fg'] == self.hint_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self._put_hint()
