from tkinter import Tk
from src.settings import BASE, ENGINE
from src.main_window import Window



def main():
    BASE.metadata.create_all(ENGINE)
    root = Tk()
    Window(root)
    root.wm_title("My app")
    root.mainloop()


if __name__ == "__main__":
    main()
