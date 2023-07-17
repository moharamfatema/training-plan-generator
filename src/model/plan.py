# imports
from week import Week, NEXT_WEEK_TYPES
from datetime import datetime, timedelta
from typing import List

# constants
WEEK_TYPES = NEXT_WEEK_TYPES.keys()

class Plan:
    def __init__(self, start_date: datetime, end_date: datetime):
        # min 8 weeks
        assert (end_date - start_date).days >= 8 * 7, "Training plan must be at least 8 weeks long"
        self.__start_date = start_date
        self.__end_date = end_date
        self.__num_weeks = (end_date - start_date).days // 7
        self.__weeks = []
        self.__generate_plan()

    def __generate_plan(self):
        # TODO: generate plan
        raise NotImplementedError

