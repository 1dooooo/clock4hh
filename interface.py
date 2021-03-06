from datetime import datetime
import tkinter
import tkinter.messagebox
import customtkinter
from time_2_select_2 import Calendar
from logger import logger

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520
    # PROGRESS = 0
    job_callback = lambda: print("before job init....")

    def __init__(self):
        super().__init__()

        self.title("clock4hh")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed 

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=5)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(2, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(10, minsize=10)    # empty row with minsize as spacing


        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="clock4hh",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)


        self.start_date=customtkinter.StringVar()		#????????????
        self.end_date=customtkinter.StringVar()	

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="????????????",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:self.start_date.set(Calendar().selection()))
        self.button_1.grid(row=3, column=0, pady=10, padx=20)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_left,
                                                textvariable=self.start_date,
                                                )
        self.entry_1.grid(row=4, column=0, pady=10, padx=20)
        self.entry_1.bind("<FocusIn>", lambda event:(
            self.start_date.set(Calendar().selection()),
            self.focus()
        ))


        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="????????????",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lambda:self.end_date.set(Calendar().selection()),
                                                )
        self.button_2.grid(row=6, column=0, pady=10, padx=20)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_left,
                                                textvariable=self.end_date,
                                                )
        self.entry_2.grid(row=7, column=0, pady=10, padx=20)
        self.entry_2.bind("<FocusIn>", lambda event:(
            self.end_date.set(Calendar().selection()),
            self.focus()
        ))


        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="??????",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_3.grid(row=8, column=0, pady=10, padx=20)


        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (2x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        # self.frame_right.rowconfigure(7, weight=1)
        self.frame_right.columnconfigure((0, 1), weight=1)


        # ============ frame_info ============
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=str(datetime.now())[:19],
                                                   height=1000,
                                                   width=1000,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   anchor=tkinter.CENTER,
                                                   text_font=('??????',30, 'bold'),
                                                   )
        self.label_info_1.grid(row=0, column=0, sticky="nswe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)


       # ============ frame_intervel ============
        self.frame_intervel = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_intervel.grid(row=4, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")


        # configure grid layout (1x1)
        self.frame_intervel.rowconfigure(0, weight=1)
        self.frame_intervel.columnconfigure(0, weight=1)
        self.frame_intervel.columnconfigure(1, weight=9)


        self.slider_1 = customtkinter.CTkSlider(master=self.frame_intervel,
                                                progress_color="pink",
                                                from_=1,
                                                to=121,
                                                number_of_steps=120,
                                                button_corner_radius=5,
                                                command=lambda value:self.label_intervel.set_text(" %03d" % int(value) + "??? "),
                                                )
        self.slider_1.grid(row=0, column=1, pady=15, padx=15, sticky="we")

        self.label_intervel = customtkinter.CTkLabel(master=self.frame_intervel,
                                                   anchor=tkinter.CENTER,
                                                   width = 50,
                                                   text="030??? ",
                                                   text_font=('??????',10, 'bold'),
                                                   corner_radius=10,
                                                   )
        self.label_intervel.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")

        # self.radio_var = tkinter.IntVar(value=0)

        # self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                  height=25,
        #                                                  text="CTkButton",
        #                                                  border_width=3,   # <- custom border_width
        #                                                  fg_color=None,   # <- no fg_color
        #                                                  command=self.button_event)
        # self.checkbox_button_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # self.entry = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="CTkEntry")
        # self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        # self.button_5 = customtkinter.CTkButton(master=self.frame_right,
        #                                         text="CTkButton",
        #                                         command=self.button_event)
        # self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # # set default values
        # self.radio_button_1.select()
        # self.switch_2.select()
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()

    def combobox_callback(self, choice):
        print("combobox dropdown clicked:", choice)

    def button_event(self):
        logger.info("job init...")
        self.job_callback()
    
    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()
    
    def updatte_process(self, progress_percent, label_text):
        self.progressbar.set(progress_percent)
        self.label_info_1.set_text(label_text)



# if __name__ == "__main__":
#     app = App()
#     app.mainloop()