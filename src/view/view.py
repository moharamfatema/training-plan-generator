"""
This module contains the GUI for the training plan generator.

Functions:
    enter_date: Creates a DateEntry widget with a label above it.
    run: Runs the GUI.
"""
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import DateEntry


class Gui:
    """Class representing the GUI for the training plan generator.

    Attributes:
        __root (Tk): The parent widget.
        __start_date (DateEntry): The DateEntry widget for the start date.
        __end_date (DateEntry): The DateEntry widget for the end date.
        __command (function): The function to run when the button is pressed.

    Methods:
        start_date (getter): Returns the start date.
        end_date (getter): Returns the end date.
        enter_date: Creates a DateEntry widget with a label above it."""

    def __init__(self, button_action) -> None:
        self.__command = button_action
        self.__root = ThemedTk(theme="breeze")
        self.__root.title("Training Plan Generator")
        self.__root.geometry("480x500")
        # self.__root.resizable(False, False)

        self.__start_date = self.__enter_date("Choose starting date", row=0)
        self.__end_date = self.__enter_date("Choose ending date", row=1)

        self.__start_button()

        self.__root.mainloop()

    @property
    def start_date(self) -> DateEntry:
        return self.__start_date

    @property
    def end_date(self) -> DateEntry:
        return self.__end_date

    def __enter_date(self, text, row):
        """Creates a DateEntry widget with a label above it.

        Args:
            self.__root (Tk): The parent widget.
            text (str): The text to display above the DateEntry widget.

        Returns:
            DateEntry: The DateEntry widget.
        """
        ttk.Label(self.__root, text=text).grid(
            row=row, column=0, padx=10, pady=10
        )

        cal = DateEntry(
            self.__root,
            width=40,
            background="purple",
            foreground="white",
            borderwidth=1,
        )
        cal.grid(row=row, column=1, padx=10, pady=10)

        # cal.pack(padx=10, pady=10)

        return cal

    def start_button_action(self):
        try:
            res = self.__command(
                self.start_date.get_date(), self.end_date.get_date()
            )

        except (AssertionError, ValueError) as err:
            res = err
        self.__display_plan(res)

    def __start_button(self):
        """Creates a button that generates the training plan.

        Args:
            command (function): The function to run when the button is pressed.

        Returns:
            Button: The button.
        """
        btn = ttk.Button(
            self.__root,
            text="Generate Training Plan",
            command=self.start_button_action,
            width=40,
        )
        btn.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        # btn.pack(padx=10, pady=10)

        return btn

    def __display_plan(self, plan):
        """Displays the training plan.

        Args:
            plan (Plan): The training plan.
        """
        lbl = ttk.Label(self.__root, text="Training Plan")
        lbl.grid(padx=10, pady=10, row=3, column=0, columnspan=2)

        out = tk.Text(self.__root, width=60)
        out.configure(state="normal")
        out.insert(tk.END, str(plan))
        out.configure(state="disabled")
        out.grid(padx=10, pady=10, row=4, column=0, columnspan=2)
        scrollbar_y = ttk.Scrollbar(
            self.__root, orient="vertical", command=out.yview
        )
        scrollbar_x = ttk.Scrollbar(
            self.__root, orient="horizontal", command=out.xview
        )
        out.config(
            yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set
        )
