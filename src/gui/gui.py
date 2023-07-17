"""
This module contains the GUI for the training plan generator.

Functions:
    enter_date: Creates a DateEntry widget with a label above it.
    run: Runs the GUI.
"""

from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import DateEntry

def enter_date(top, text):
    """Creates a DateEntry widget with a label above it.

    Args:
        top (Tk): The parent widget.
        text (str): The text to display above the DateEntry widget.

    Returns:
        DateEntry: The DateEntry widget.
    """
    ttk.Label(top, text=text).pack(padx=10, pady=10)

    cal = DateEntry(
        top, width=20, background="purple", foreground="white", borderwidth=1
    )

    cal.pack(padx=10, pady=10)

    return cal


def run():
    """Runs the GUI."""
    root = ThemedTk(theme="breeze")
    root.title("Training Plan Generator")
    root.geometry("500x500")
    root.resizable(False, False)

    ### Input fields ###
    start_date = enter_date(root, "Choose starting date")
    end_date = enter_date(root, "Choose ending date")

    # Start button
    start_button = ttk.Button(
        root,
        text="Generate Training Plan",
        command=lambda *args: print(
            "Start button pressed", start_date.get_date(), end_date.get_date()
        ),
        # TODO: Add functionality to button
    )
    start_button.pack(padx=10, pady=10)

    root.mainloop()

    print(start_date.get_date())
    print(end_date.get_date())
