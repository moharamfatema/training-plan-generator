"""
Module for the Week class.

This module contains the Week class, which represents a week of training.

Classes:
    Week: A week of training.
"""

# imports
from datetime import datetime, timedelta

# constants
TEST = "Test"
FILLER = "Filler"
RECOVERY = "Recovery"
BUILD_1 = "Build 1"
BUILD_2 = "Build 2"
KEY = "Key"
TAPER = "Taper"
RACE = "Race"

WEEK_TYPES = {
    TEST,
    FILLER,
    RECOVERY,
    BUILD_1,
    BUILD_2,
    KEY,
    TAPER,
    RACE,
}


class Week:
    """A week of training.

    Attributes:
        number (int): The week number.
        start (datetime): The start date of the week.
        end (datetime): The end date of the week.
        type (str): The type of week.
    """

    def __init__(self, number: int, start: datetime, week_type: str):
        assert week_type in WEEK_TYPES, f"Invalid week type: {week_type}"
        assert number > 0, f"Invalid week number: {number}"

        self.__number = number
        self.__start = start
        self.__type = week_type

    @property
    def number(self) -> int:
        return self.__number

    @property
    def start(self) -> datetime:
        return self.__start

    @property
    def end(self) -> datetime:
        return self.__start + timedelta(days=6)

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, week_type: str) -> None:
        assert week_type in WEEK_TYPES, f"Invalid week type: {week_type}"
        self.__type = week_type

    def __str__(self) -> str:
        return f"Week #{self.number} \t- {self.type} \t\
                - from {self.start.strftime('%d %b')} \t\
                    to {self.end.strftime('%d %b')}"

    def __repr__(self) -> str:
        return self.__str__()
