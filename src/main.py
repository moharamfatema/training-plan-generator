"""
Main file for the application.
"""
from datetime import datetime
from model.plan import Plan
from gui.gui import Gui

GUI_ENABLED = True


class Controller:
    """Controller class for the application."""

    def __init__(self):
        if GUI_ENABLED:
            Gui(Controller.generate_plan)
        else:
            # for manual testing:
            print(
                Controller.generate_plan(
                    # modfy below this line
                    start_date=datetime(2021, 5, 30),
                    end_date=datetime(2021, 8, 14)
                    # modify above this line
                )
            )

    @staticmethod
    def generate_plan(
        start_date: datetime,
        end_date: datetime,
    ):
        """Generates a plan based on the given start and end dates."""
        return Plan(start_date, end_date)


if __name__ == "__main__":
    Controller()
