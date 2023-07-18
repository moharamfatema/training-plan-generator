"""
Module for the Week class.

This module contains the Week class, which represents a week in a training plan.

Classes:
    WeekTypes : Enum representing the types of weeks in a training plan.
"""

# imports
from enum import Enum


class WeekTypes(Enum):
    """Enum representing the types of weeks in a training plan."""

    TEST = "Test"
    FILLER = "Filler"
    RECOVERY = "Recovery"
    BUILD_1 = "Build 1"
    BUILD_2 = "Build 2"
    KEY = "Key"
    TAPER = "Taper"
    RACE = "Race"
