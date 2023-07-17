"""
Main file for the application.
"""
from datetime import datetime
from model.plan import Plan
from gui.gui import run

if __name__ == "__main__":
    # run()
    start_date = datetime(2021, 6, 6)
    end_date = datetime(2021, 8, 14)

    plan = Plan(start_date, end_date)
    print(plan)
