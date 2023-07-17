"""
"""

# imports
from datetime import datetime, timedelta
from typing import List, Optional

# constants
TEST = "Test"
FILLER = "Filler"
RECOVERY = "Recovery"
BUILD_1 = "Build 1"
BUILD_2 = "Build 2"
KEY = "Key"
TAPER = "Taper"
RACE = "Race"

NEXT_WEEK_TYPES = {
    TEST: {TEST,FILLER, RECOVERY},
    FILLER: {RECOVERY},
    RECOVERY: {BUILD_1},
    BUILD_1: {BUILD_2},
    BUILD_2: {KEY},
    KEY: {RECOVERY, TAPER},
    TAPER: {RACE},
    RACE: {}
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
        assert week_type in NEXT_WEEK_TYPES.keys, f"Invalid week type: {week_type}"
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
        assert week_type in NEXT_WEEK_TYPES.keys, f"Invalid week type: {week_type}"
        self.__type = week_type

    def __str__(self) -> str:
        return f"Week #{self.number} - {self.type} - from {self.start} to {self.end}"

    def get_next_week_types(self) -> str:
        return NEXT_WEEK_TYPES[self.type]
