"""
Main file for the application.
"""
from datetime import datetime
from model.plan import Plan
from gui.gui import Gui


class Controller:
    def __init__(self):
        Gui(Controller.generate_plan)

    @staticmethod
    def generate_plan(
        start_date: datetime,
        end_date: datetime,
    ):
        return Plan(start_date, end_date)


if __name__ == "__main__":
    controller = Controller()
    # for manual testing:
    #  print(
    #     Controller.generate_plan(
    #         datetime(2020, 6, 1),
    #         datetime(2021, 8, 14)
    #     )
    # )

