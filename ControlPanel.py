from tkinter import *
from tkinter import colorchooser

from CONSTANTS import OUT_CLR, CTRL_PNL_HGT, CTRL_PNL_WDT, TICK_INT
from CONSTANTS import X_THETA, Y_THETA, Z_THETA
from UtilityFunctions import to_deg


class ControlPanel(Frame):
    def __init__(self, master=None, width=CTRL_PNL_WDT, height=CTRL_PNL_HGT):
        super(ControlPanel, self).__init__(master=master, width=width, height=height)
        self.config(padx=10, pady=10)
        self.config(highlightthickness=1, highlightbackground=OUT_CLR)

        Label(self, text='Cube Display Controls', font='TkDefaultFont 10 bold').grid(row=0, column=0,
                                                                                     columnspan=3, sticky=W)

        self.show_clrs = BooleanVar(value=True)
        self.ck_clrs = Checkbutton(self, text="Show colors", variable=self.show_clrs, selectcolor='BLACK',
                                   command=lambda *args: self.event_generate("<<Show Color Change>>")
                                   ).grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.show_outline = BooleanVar(value=False)
        self.ck_outline = Checkbutton(self, text="Show outline", variable=self.show_outline, selectcolor='BLACK',
                                      command=lambda *args: self.event_generate("<<Show Outline Change>>")
                                      ).grid(row=1, column=1, padx=10, pady=10, sticky=W)

        self.show_points = BooleanVar(value=False)
        self.ck_dots = Checkbutton(self, text="Show points", variable=self.show_points, selectcolor='BLACK',
                                   command=lambda *args: self.event_generate("<<Show Points Change>>")
                                   ).grid(row=1, column=2, padx=10, pady=10, sticky=W)

        self.ck_dots = Button(self, text="Reset Perspective",
                              command=lambda *args: self.event_generate("<<reset canvas>>")
                              ).grid(row=1, column=3, padx=10, pady=10, sticky=W)

        Label(self, text='Axial Rotation Controls', font='TkDefaultFont 10 bold').grid(row=2, column=0, columnspan=3,
                                                                                       pady=(10, 0), sticky=W)
        Label(self, text='X°:').grid(row=3, column=0, sticky=EW, pady=10)
        Label(self, text='Y°:').grid(row=4, column=0, sticky=EW, pady=10)
        Label(self, text='Z°:').grid(row=5, column=0, sticky=EW, pady=10)

        self.xchange = DoubleVar(value=to_deg(X_THETA))
        self.ychange = DoubleVar(value=to_deg(Y_THETA))
        self.zchange = DoubleVar(value=to_deg(Z_THETA))

        self.sc_xchange = Scale(self, from_=-360, to_=360, orient=HORIZONTAL, variable=self.ychange,
                                command=lambda *args: self.event_generate('<<x-change>>'),
                                tickinterval=TICK_INT)
        self.sc_xchange.grid(row=3, column=1, sticky=EW, columnspan=3)

        self.sc_ychange = Scale(self, from_=-360, to_=360, orient=HORIZONTAL, variable=self.xchange,
                                command=lambda *args: self.event_generate('<<y-change>>'),
                                tickinterval=TICK_INT)
        self.sc_ychange.grid(row=4, column=1, sticky=EW, columnspan=3)

        self.sc_zchange = Scale(self, from_=-360, to_=360, orient=HORIZONTAL, variable=self.zchange,
                                command=lambda *args: self.event_generate('<<z-change>>'),
                                tickinterval=TICK_INT)
        self.sc_zchange.grid(row=5, column=1, sticky=EW, columnspan=3)

