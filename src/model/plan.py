# imports
from .week import (
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
from datetime import datetime, timedelta
from typing import List

# constants
PLAN_0 = 0
PLAN_1 = 1
PLAN_2 = 2
PLAN_3 = 3

MAIN_WEEK_TYPES = [RECOVERY, BUILD_1, BUILD_2, KEY]


class Plan:
    def __init__(self, start_date: datetime, end_date: datetime):
        # min 8 weeks
        assert (
            end_date - start_date
        ).days >= 8 * 7, "Training plan must be at least 8 weeks long"
        self.__end_date = end_date

        # * assumption : race day is always n weeks away from start day (no partial weeks)
        self.__num_weeks = (1 + (end_date - start_date).days )// 7
        print("num weeks : ",self.__num_weeks) # debug
        self.__start_date = start_date
        self.__current_date = self.__start_date

        self.__weeks = []
        self.__generate_plan()

    def __get_plan_type(self):
        weeks_remaining = (self.__num_weeks - 8) % 4
        if weeks_remaining == 0:
            return PLAN_0
        elif weeks_remaining == 1:
            return PLAN_1
        elif weeks_remaining == 2:
            return PLAN_2
        else:
            return PLAN_3

    def __generate_main_block(self, start_count) -> list[Week]:
        weeks = []
        for week_type in MAIN_WEEK_TYPES:
            weeks.append(Week(start_count, self.__current_date, week_type))
            self.__current_date += timedelta(days=7)
            start_count += 1
        return weeks

    def __generate_first_main_week(
        self, start_count, plan_type: int
    ) -> list[Week]:
        weeks: list[Week] = []
        if plan_type == PLAN_0:
            return self.__generate_main_block(start_count)
        elif plan_type == PLAN_1:
            self.__current_date += timedelta(days=7)
            filler_week = Week(start_count, self.__current_date, FILLER)
            start_count += 1
            main_weeks = self.__generate_main_block(start_count)
            weeks = [filler_week] + main_weeks
        elif plan_type == PLAN_2:
            self.__current_date -= timedelta(days=2 * 7)
            weeks = self.__generate_main_block(start_count)
            weeks = weeks[2:]
        elif plan_type == PLAN_3:
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

        # get plan type
        plan_type = self.__get_plan_type()
        print("plan type : ",plan_type) # debug

        num_main_blocks = (self.__num_weeks - 4) // 4

        if plan_type != PLAN_0:
            # generate first main block
            main_weeks = self.__generate_first_main_week(count, plan_type)
            self.__weeks += main_weeks
            count += len(main_weeks)

        # generate next main blocks
        for _ in range(num_main_blocks):
            weeks = self.__generate_main_block(count)
            self.__weeks += weeks
            count += 4

        # generate final weeks
        self.__weeks.append(Week(count, self.__current_date, TAPER))
        count += 1
        self.__current_date += timedelta(days=7)
        self.__weeks.append(Week(count, self.__current_date, RACE))
        assert (
            count == self.__num_weeks
        ), f"Internal Error : Incorrect number of weeks generated\n Expected : {self.__num_weeks}\n Actual : {count}"
        # assert (
        #     self.__current_date == self.__end_date
        # ), "Internal Error : Incorrect end date generated"
        # assert (
        #     self.__weeks[-1] == self.__end_date
        # ), "Internal Error : Incorrect end date generated"

    @property
    def weeks(self) -> List[Week]:
        return self.__weeks

    def __str__(self) -> str:
        return "\n".join([str(week) for week in self.__weeks])

    def __repr__(self) -> str:
        return str(self)
