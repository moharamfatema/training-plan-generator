# imports
from datetime import datetime, timedelta
from typing import List
from model.week import (
    Week,
    TEST,
    FILLER,
    RECOVERY,
    BUILD_1,
    BUILD_2,
    KEY,
    TAPER,
    RACE,
)

# constants
PLAN_0 = 0  # 4 + 4n weeks
PLAN_1 = 1  # 5 + 4n weeks
PLAN_2 = 2  # 6 + 4n weeks
PLAN_3 = 3  # 7 + 4n weeks

MAIN_WEEK_TYPES = [RECOVERY, BUILD_1, BUILD_2, KEY]


class Plan:
    """Class representing a training plan.

    Attributes:
        start_date (datetime): The start date of the training plan.
        end_date (datetime): The end date of the training plan.
        num_weeks (int): The number of weeks in the training plan.
        weeks (list[Week]): The weeks in the training plan.

    Methods:
        weeks (getter): Returns the weeks in the training plan.
    """

    def __init__(self, start_date: datetime, end_date: datetime):
        # min 8 weeks
        assert (
            end_date - start_date
        ).days >= 8 * 7, "Training plan must be at least 8 weeks long"
        self.__end_date = end_date

        # * assumption : race day id either exactly n days from start day
        # or start day will be modified to fit the criteria

        diff = (end_date - start_date).days + 1
        if diff % 7 != 0:
            self.__start_date = start_date + timedelta(days=diff % 7)
            print(
                f"Warning : Start date modified to fit training plan\n\
            Original start date : {start_date}\n\
            New start date : {self.__start_date}"
            )
        else:
            self.__start_date = start_date

        self.__num_weeks = (1 + (self.__end_date - self.__start_date).days) // 7

        self.__current_date = self.__start_date
        self.__plan_type = self.__get_plan_type()

        self.__weeks = []
        self.__generate_plan()

    def __get_plan_type(self):
        """Returns the plan type based on the number of weeks."""
        weeks_remaining = (self.__num_weeks - 8) % 4
        if weeks_remaining == 0:
            return PLAN_0
        if weeks_remaining == 1:
            return PLAN_1
        if weeks_remaining == 2:
            return PLAN_2
        return PLAN_3

    def __generate_main_block(self, start_count) -> list[Week]:
        """Generates a main block of 4 weeks.
        Week 1 : Recovery
        Week 2 : Build 1
        Week 3 : Build 2
        Week 4 : Key
        """
        weeks = []
        for week_type in MAIN_WEEK_TYPES:
            weeks.append(Week(start_count, self.__current_date, week_type))
            self.__current_date += timedelta(days=7)
            start_count += 1
        return weeks

    def __generate_first_main_block(self, start_count) -> list[Week]:
        weeks: list[Week] = []
        if self.__plan_type == PLAN_1:
            # generate filler week
            self.__current_date += timedelta(days=7)
            filler_week = Week(start_count, self.__current_date, FILLER)
            start_count += 1
            weeks = [filler_week]
        elif self.__plan_type == PLAN_2:
            # generate half main block
            self.__current_date -= timedelta(days=2 * 7)
            weeks = self.__generate_main_block(start_count)
            weeks = weeks[2:]
        elif self.__plan_type == PLAN_3:
            # generate main block minus 1 week
            self.__current_date -= timedelta(days=7)
            weeks = self.__generate_main_block(start_count)
            weeks = weeks[1:]
        return weeks

    def __generate_plan(self):
        # start with 2 test weeks
        count = 1
        for _ in range(2):
            self.__weeks.append(Week(count, self.__current_date, TEST))
            self.__current_date += timedelta(days=7)
            count += 1

        num_main_blocks = (self.__num_weeks - 4) // 4
        print(f"num_main_blocks : {num_main_blocks}")

        if self.__plan_type != PLAN_0:
            # generate first block
            main_weeks = self.__generate_first_main_block(count)
            self.__weeks += main_weeks
            count += len(main_weeks)

        # generate next main blocks
        for _ in range(num_main_blocks):
            weeks = self.__generate_main_block(count)
            self.__weeks += weeks
            count += 4

        # generate last 2 weeks
        self.__weeks.append(Week(count, self.__current_date, TAPER))
        count += 1
        self.__current_date += timedelta(days=7)
        self.__weeks.append(Week(count, self.__current_date, RACE))
        self.__current_date += timedelta(days=6)

        assert (
            count == self.__num_weeks
        ), f"Internal Error : Incorrect number of weeks generated\n\
              Expected : {self.__num_weeks}\n Actual : {count}"
        assert (
            self.__current_date == self.__end_date
        ), f"Internal Error : Incorrect end date generated\n\
                Expected : {self.__end_date}\n Actual : {self.__current_date}"
        assert (
            self.__weeks[-1].end == self.__end_date
        ), f"Internal Error : Incorrect end date generated\n\
                Expected : {self.__end_date}\n Actual : {self.__weeks[-1].end}"

    @property
    def weeks(self) -> List[Week]:
        """Returns the weeks in the training plan."""
        return self.__weeks

    def __str__(self) -> str:
        """Returns a string representation of the training plan."""
        return "\n".join([str(week) for week in self.__weeks])

    def __repr__(self) -> str:
        """Returns a string representation of the training plan."""
        return str(self)
