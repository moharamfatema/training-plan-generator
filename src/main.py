"""
Main file for the application.
"""
from datetime import datetime
from model.plan import Plan
from gui.gui import Gui

class Controller:
    def __init__(self):
        self.__plan = None
        self.__gui = Gui(self.generate_plan)

    def generate_plan(
            self,
            start_date: datetime,
            end_date: datetime,
    ):
        self.__plan = Plan(start_date, end_date)
        return self.__plan



if __name__ == "__main__":
    controller = Controller()
