from tkinter import BOTTOM, Frame, Menu, Label
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from src.database import DataBase
from src.analizator import Analizator
from src.settings import DATASET, JSON_FILENAME, SESSION



class Window(Frame):
    data_base = DataBase(DATASET, JSON_FILENAME, SESSION)
    analizator = Analizator(SESSION)
    error_colour = "red"
    success_colour = "green"
    info_colour = "white"

    def __init__(self, master, width="1200", height="900"):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry(f"{width}x{height}")

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.data_label = Label(master, text="Aggregation..")
        self.data_label.pack()
        self.figure = Figure(figsize=(20, 18), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self.master)
        self.status_label = Label(master, text="Result of last operation")
        self.status_label.pack(side=BOTTOM)

        db_menu = Menu(self.menu)
        db_menu.add_command(label="Clear database", command=self.clear_db)
        db_menu.add_command(label="Fill database", command=self.download_data_to_db)
        self.menu.add_cascade(label="File", menu=db_menu)

        data_menu = Menu(self.menu)
        data_menu.add_command(
            label="Displays an aggregation", command=self.show_aggregation
        )
        data_menu.add_command(label="Show chart", command=self.show_chart)
        self.menu.add_cascade(label="Data", menu=data_menu)

    def clear_db(self):
        self.data_base.empty()
        self.status_label.config(text="Databse was emptied", bg=self.success_colour)

    def download_data_to_db(self):
        if not self.data_base.is_empty:
            self.status_label.config(text="Databse is not empty", bg=self.error_colour)
            return
        self.data_base.fill()
        self.status_label.config(text="New data was loaded", bg=self.success_colour)

    def show_aggregation(self):
        if self.data_base.is_empty:
            self.status_label.config(
                text="Databse is empty, cannot read data", bg=self.error_colour
            )
            return
        data = self.analizator.aggregation
        self.data_label.config(text=f"Average male to female ratio {data}")
        self.status_label.config(text=f"Calculated aggregation", bg=self.info_colour)

    def show_chart(self):
        if self.data_base.is_empty:
            self.status_label.config(
                text="Databse is empty, cannot read data", bg=self.error_colour
            )
            return
        data = self.analizator.chart_data

        axis = self.figure.add_subplot(111)
        axis.plot(*data)
        axis.set_title("Percentage of international students per uni")

        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.status_label.config(text=f"Finalized creating chart", bg=self.info_colour)