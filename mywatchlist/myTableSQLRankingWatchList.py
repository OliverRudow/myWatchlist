"""myTableSQLRankingWatchList.py."""

__title__: str = "myTableSQLRankingWatchList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import mySQLDataBase, myTableSQL
from mysharesdefinition import myRankingWatchListDefinitions, myAnalystWatchListDefinitions, myDerivateWatchListDefinitions, \
    myFundamentalsWatchListDefinitions, myPerformanceWatchListDefinitions, myCalendarWatchListDefinitions, myStaticWatchListDefinitions


@dataclasses.dataclass(init=False)
class MyTableSQLRankingWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_ranking_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_ranking_watch_list_quote_isin_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_analyst_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_derivate_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_fundamentals_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_performance_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_overall_score_column_index: int = dataclasses.field(repr=False, default=0)
    _int_ranking_watch_list_shift_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_ranking_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_analyst_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_derivate_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_fundamentals_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_performance_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_overall_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_shift_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_ranking_watch_list_quote_isin_value: str = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_analyst_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_derivate_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_fundamentals_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_performance_score_value: str | float = dataclasses.field(repr=False, default='')
    _float_ranking_watch_list_overall_score_value: str | float = dataclasses.field(repr=False, default='')
    _int_ranking_watch_list_shift_value: str | int = dataclasses.field(repr=False, default='')

    # source tables
    _str_source_table_name_analyst_eval: str = dataclasses.field(repr=False, default="")
    _str_source_table_analyst_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_analyst_absolute_score_column_name: str = dataclasses.field(repr=False, default='')

    _str_source_table_name_derivate_eval: str = dataclasses.field(repr=False, default="")
    _str_source_table_derivate_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_derivate_absolute_score_column_name: str = dataclasses.field(repr=False, default='')

    _str_source_table_name_fundamentals_eval: str = dataclasses.field(repr=False, default="")
    _str_source_table_fundamentals_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_fundamentals_surprise_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_fundamentals_ratio_dividend_yield_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_fundamentals_absolute_score_column_name: str = dataclasses.field(repr=False, default='')

    _str_source_table_name_performance_eval: str = dataclasses.field(repr=False, default="")
    _str_source_table_performance_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_performance_absolute_score_column_name: str = dataclasses.field(repr=False, default='')

    _str_source_table_name_calendar: str = dataclasses.field(repr=False, default="")
    _str_source_table_calendar_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_calendar_earnings_delta_date_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_calendar_ex_dividend_delta_date_column_name: str = dataclasses.field(repr=False, default='')

    _str_source_table_name_static: str = dataclasses.field(repr=False, default="")
    _str_source_table_static_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_static_quote_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_table_static_quote_industry_column_name: str = dataclasses.field(repr=False, default='')

    # score table
    _str_score_table_name: str = dataclasses.field(repr=False, default='')
    _str_score_table_weight_column_name: str = dataclasses.field(repr=False, default='')
    _str_score_table_weight_name_column_name: str = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myRankingWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME)

        # column quote isin
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column analyst score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column derivate score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fundamentals score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column performance score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column overall score
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column shift
        my_special_tuple = myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN)

        # generata a copy of the ranking watch list table
        if self.check_sql_data_base_table_exists():

            if self.check_sql_data_base_table_exists(myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_COPY):

                self.drop_sql_table(myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_COPY)

            self.create_sql_data_base_table(myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_COPY)

            self._sql_table_create_copy()

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_ranking_watch_list_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        self._init_source_table_analyst()

        self._init_source_table_derivate()

        self._init_source_table_fundamentals()

        self._init_source_table_performance()

        self._init_source_table_calendar()

        self._init_source_table_static()

        self._init_score_table()

    def _init_ranking_watch_list_columns(self) -> None:

        self._str_ranking_watch_list_quote_isin_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN)

        self._int_ranking_watch_list_quote_isin_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN)

        self._str_ranking_watch_list_analyst_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE)

        self._int_ranking_watch_list_analyst_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE)

        self._str_ranking_watch_list_derivate_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE)

        self._int_ranking_watch_list_derivate_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE)

        self._str_ranking_watch_list_fundamentals_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE)

        self._int_ranking_watch_list_fundamentals_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE)

        self._str_ranking_watch_list_performance_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE)

        self._int_ranking_watch_list_performance_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE)

        self._str_ranking_watch_list_overall_score_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE)

        self._int_ranking_watch_list_overall_score_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE)

        self._str_ranking_watch_list_shift_column_name = self.get_column_name_from_dict(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT)

        self._int_ranking_watch_list_shift_column_index = self.get_column_index_from_list(
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT)

    def _init_source_table_analyst(self) -> None:
        self._str_source_table_name_analyst_eval = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_ANALYST

        self._str_source_table_analyst_quote_isin_column_name = (
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_EVAL_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_source_table_analyst_absolute_score_column_name = (
            myAnalystWatchListDefinitions.TUPLE_ANALYST_WATCH_LIST_EVAL_ABSOLUTE_SCORE[self._index_tuple.DATA_CONTENT][0])

    def _init_source_table_derivate(self) -> None:
        self._str_source_table_name_derivate_eval = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_DERIVATE

        self._str_source_table_derivate_quote_isin_column_name = (
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_EVAL_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_source_table_derivate_absolute_score_column_name = (
            myDerivateWatchListDefinitions.TUPLE_DERIVATE_WATCH_LIST_EVAL_ABSOLUTE_SCORE[self._index_tuple.DATA_CONTENT][
                0])

    def _init_source_table_fundamentals(self) -> None:
        self._str_source_table_name_fundamentals_eval = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_FUNDAMENTALS

        self._str_source_table_fundamentals_quote_isin_column_name = (
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_source_table_fundamentals_surprise_credit_column_name = (
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_SURPRISE_CREDIT)[self._index_tuple.DATA_CONTENT][0]

        self._str_source_table_fundamentals_ratio_dividend_yield_column_name = (
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_RATIO_DIVIDEND_YIELD)[self._index_tuple.DATA_CONTENT][0]

        self._str_source_table_fundamentals_absolute_score_column_name = (
            myFundamentalsWatchListDefinitions.TUPLE_FUNDAMENTALS_WATCH_LIST_EVAL_ABSOLUTE_SCORE[self._index_tuple.DATA_CONTENT][
                0])

    def _init_source_table_performance(self) -> None:
        self._str_source_table_name_performance_eval = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_PERFORMANCE

        self._str_source_table_performance_quote_isin_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_source_table_performance_absolute_score_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE[self._index_tuple.DATA_CONTENT][
                0])

    def _init_source_table_calendar(self) -> None:

        self._str_calendar_data_base_file_name: str = '/Users/oliverrudow/PycharmProjects/Data/shares_data_base.db'

        self._str_source_table_name_calendar: str = myCalendarWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._str_source_table_calendar_quote_isin_column_name: str = (
            myCalendarWatchListDefinitions.TUPLE_CALENDAR_WATCH_LIST_QUOTE_ISIN)[self._index_tuple.DATA_CONTENT][0]

        self._str_source_table_calendar_earnings_delta_date_column_name: str = (
            myCalendarWatchListDefinitions.TUPLE_CALENDAR_WATCH_LIST_EARNINGS_DELTA_DATE)[self._index_tuple.DATA_CONTENT][0]

        self._str_source_table_calendar_ex_dividend_delta_date_column_name: str = (
            myCalendarWatchListDefinitions.TUPLE_CALENDAR_WATCH_LIST_EX_DIVIDEND_DELTA_DATE)[self._index_tuple.DATA_CONTENT][0]

    def _init_source_table_static(self) -> None:

        self._str_source_table_name_static = myStaticWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._str_source_table_static_quote_isin_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN)[self._index_tuple.DATA_CONTENT][0]

        self._str_source_table_static_quote_name_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_NAME)[self._index_tuple.DATA_CONTENT][0]

        self._str_source_table_static_quote_industry_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_INDUSTRY)[self._index_tuple.DATA_CONTENT][0]

    def _init_score_table(self):
        self._str_score_table_name = myRankingWatchListDefinitions.STR_SCORE_TABLE_NAME

        self._str_score_table_weight_name_column_name = (
            myRankingWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT_NAME)[
            self._index_tuple.DATA_CONTENT][0]

        self._str_score_table_weight_column_name = (
            myRankingWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT)[
            self._index_tuple.DATA_CONTENT][0]

    def _set_score_table(self, list_score_table_data: list[tuple]) -> None:

        self.drop_sql_table(self._str_score_table_name)

        _first_column = ()

        _first_column = myRankingWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT_NAME[
                self._index_tuple.DATA_CONTENT]

        _second_column = ()

        _second_column = myRankingWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT[
                self._index_tuple.DATA_CONTENT]


        my_list: list = [' '.join(_first_column), ' '.join(_second_column)]

        str_table_definition = ', '.join(my_list)

        str_text = (f'CREATE TABLE IF NOT EXISTS {self._str_score_table_name} '
                    f'({str_table_definition})')

        str_text_insert = f'INSERT INTO {self._str_score_table_name} VALUES (?, ?) '

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_cursor.executemany(str_text_insert, list_score_table_data)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._set_score_table.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _update_ranking_table(self) -> None:

        # copy quote isin column
        self._insert_data_from_source_watch_list(self._str_source_table_name_analyst_eval,
                                                 self._str_source_table_analyst_quote_isin_column_name,
                                                 self._str_ranking_watch_list_quote_isin_column_name)

        # update analyst score
        self._update_data_from_source_watch_list(self._str_source_table_name_analyst_eval,
                                                 self._str_source_table_analyst_absolute_score_column_name,
                                                 self._str_source_table_analyst_quote_isin_column_name,
                                                 self._str_ranking_watch_list_analyst_score_column_name)

        # update derivate score
        self._update_data_from_source_watch_list(self._str_source_table_name_derivate_eval,
                                                 self._str_source_table_derivate_absolute_score_column_name,
                                                 self._str_source_table_derivate_quote_isin_column_name,
                                                 self._str_ranking_watch_list_derivate_score_column_name)

        # update fundamentals score
        self._update_data_from_source_watch_list(self._str_source_table_name_fundamentals_eval,
                                                 self._str_source_table_fundamentals_absolute_score_column_name,
                                                 self._str_source_table_fundamentals_quote_isin_column_name,
                                                 self._str_ranking_watch_list_fundamentals_score_column_name)

        # update performance score
        self._update_data_from_source_watch_list(self._str_source_table_name_performance_eval,
                                                 self._str_source_table_performance_absolute_score_column_name,
                                                 self._str_source_table_performance_quote_isin_column_name,
                                                 self._str_ranking_watch_list_performance_score_column_name)

    def _insert_data_from_source_watch_list(self, str_source_table_name: str,
                                         str_source_column_name: str, str_target_column_name: str) -> None:

        _str_source_table_name = str_source_table_name

        _str_source_column_name = str_source_column_name

        _str_target_column_name = str_target_column_name

        str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name} '
                    f'({_str_target_column_name}) '
                    f'SELECT {_str_source_column_name} '
                    f'FROM {str_source_table_name}')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._insert_data_from_source_watch_list.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _update_data_from_source_watch_list(self, str_source_table_name: str,
                                           str_source_column_name: str,
                                           str_source_reference_column_name: str,
                                           str_target_column_name: str) -> None:

        _target_table: str = self._str_table_name
        _source_table: str = str_source_table_name
        _target_col: str = str_target_column_name
        _source_col: str = str_source_column_name
        _target_ref: str = self._str_ranking_watch_list_quote_isin_column_name
        _source_ref: str = str_source_reference_column_name

        str_text = (f'UPDATE {_target_table} AS t '
                    f' SET {_target_col} = ('
                    f' SELECT {_source_col} FROM {_source_table} AS s '
                    f' WHERE s.{_source_ref} = t.{_target_ref})')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._update_data_from_source_watch_list.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _evaluate_absolute_score_credit(self) -> None:

        # generate score table
        self._set_score_table(myRankingWatchListDefinitions.LIST_WEIGHT_SCORE_TABLE)

        _score = self._str_score_table_name

        _score_first_col = myRankingWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT_NAME[
            self._index_tuple.DATA_CONTENT][0]

        _score_second_col = myRankingWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT[
            self._index_tuple.DATA_CONTENT][0]

        _table = self._str_table_name

        _result = self._str_ranking_watch_list_overall_score_column_name

        value_1 = self._str_ranking_watch_list_analyst_score_column_name

        value_2 = self._str_ranking_watch_list_derivate_score_column_name

        value_3 = self._str_ranking_watch_list_fundamentals_score_column_name

        value_4 = self._str_ranking_watch_list_performance_score_column_name

        str_text = (f'UPDATE {_table} '
                    f'SET {_result} = ROUND(CAST('
                    f'('
                    f'COALESCE({value_1} * s.w_1, 0) + '
                    f'COALESCE({value_2} * s.w_2, 0) + '
                    f'COALESCE({value_3} * s.w_3, 0) + '
                    f'COALESCE({value_4} * s.w_4, 0)) AS REAL '
                    f') '
                    f'/ '
                    f'CAST('
                    f'(CASE WHEN {value_1} IS NOT NULL THEN s.w_1 ELSE 0 END) + '
                    f'(CASE WHEN {value_2} IS NOT NULL THEN s.w_2 ELSE 0 END) + '
                    f'(CASE WHEN {value_3} IS NOT NULL THEN s.w_3 ELSE 0 END) + '
                    f'(CASE WHEN {value_4} IS NOT NULL THEN s.w_4 ELSE 0 END) '
                    f'AS REAL), 1) '
                    f'FROM '
                    f'( '
                    f'SELECT '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_1\' ) AS w_1, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_2\' ) AS w_2, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_3\' ) AS w_3, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_4\' ) AS w_4 '
                    f') '
                    f'AS s '
                    f'WHERE ('
                    f'{value_1} IS NOT NULL OR '
                    f'{value_2} IS NOT NULL OR '
                    f'{value_3} IS NOT NULL OR '
                    f'{value_4} IS NOT NULL '
                    f')')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

            self.drop_sql_table(self._str_score_table_name)

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._evaluate_absolute_score_credit.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _sql_table_create_copy(self) -> None:

        str_table_name_copy: str = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_COPY

        str_text: str = f'INSERT INTO {str_table_name_copy} SELECT * FROM {self._str_table_name}'

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._sql_table_create_copy.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _evaluate_ranking_shift(self) -> None:

        str_table_name_copy: str = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME_COPY

        str_table_name: str = self._str_table_name

        str_id: str = self._str_ranking_watch_list_quote_isin_column_name

        str_value: str = self._str_ranking_watch_list_overall_score_column_name

        str_result: str = self._str_ranking_watch_list_shift_column_name

        str_text: str = (f'WITH shift_calculation AS ( '
            f' SELECT ' 
            f' t_1.{str_id}, '
            f' COALESCE(ROW_NUMBER() OVER (ORDER BY t_2.{str_value} DESC), 0) ' 
            f' - ROW_NUMBER() OVER (ORDER BY t_1.{str_value} DESC) AS row_id_diff '
            f' FROM {str_table_name} t_1 '
            f' LEFT JOIN {str_table_name_copy} t_2 ON t_1.{str_id} = t_2.{str_id} '
            f' )'
            f' UPDATE {str_table_name} '
            f' SET {str_result} = s_c.row_id_diff '
            f' FROM shift_calculation s_c '
            f' WHERE {str_table_name}.{str_id} = s_c.{str_id}')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._evaluate_ranking_shift.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

        self.drop_sql_table(str_table_name_copy)

    def _get_sql_table_ranking_watch_list_quote_per_isin(self, str_isin: str) -> bool:

        if self._bool_sql_data_base_table:

            str_text = (f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name} '

                        f'WHERE {self._str_ranking_watch_list_quote_isin_column_name} = "{str_isin}"')

            bool_result = False

            if self._my_sql_connection and self._my_sql_cursor:

                try:

                    self._my_sql_cursor.execute(str_text)

                    tuple_result = self._my_sql_cursor.fetchone()

                    if tuple_result is not None:

                        bool_result = True

                        self._float_ranking_watch_list_analyst_score_value = tuple_result[
                            self._int_ranking_watch_list_analyst_score_column_index]

                        self._float_ranking_watch_list_derivate_score_value = tuple_result[
                            self._int_ranking_watch_list_derivate_score_column_index]

                        self._float_ranking_watch_list_fundamentals_score_value = tuple_result[
                            self._int_ranking_watch_list_fundamentals_score_column_index]

                        self._float_ranking_watch_list_performance_score_value = tuple_result[
                            self._int_ranking_watch_list_performance_score_column_index]

                        self._float_ranking_watch_list_overall_score_value = tuple_result[
                            self._int_ranking_watch_list_overall_score_column_index]

                        self._int_ranking_watch_list_shift_value = tuple_result[
                            self._int_ranking_watch_list_shift_column_index]

                    else:

                        self._float_ranking_watch_list_analyst_score_value = ''

                        self._float_ranking_watch_list_derivate_score_value = ''

                        self._float_ranking_watch_list_fundamentals_score_value = ''

                        self._float_ranking_watch_list_performance_score_value = ''

                        self._float_ranking_watch_list_overall_score_value = ''

                        self._int_ranking_watch_list_shift_value = ''

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError as err:

                    print(
                        f'---- Operational Error in {__title__}, '
                        f'{self._get_sql_table_ranking_watch_list_quote_per_isin.__name__} ----, \n'
                        f'---- the Text {str_text} has caused an Error {err} ! ----')

                    exit(1)

            return bool_result

        else:

            self._float_ranking_watch_list_analyst_score_value = ''

            self._float_ranking_watch_list_derivate_score_value = ''

            self._float_ranking_watch_list_fundamentals_score_value = ''

            self._float_ranking_watch_list_performance_score_value = ''

            self._float_ranking_watch_list_overall_score_value = ''

            self._int_ranking_watch_list_shift_value = ''

            return False

    def evaluate_overall_credits(self) -> None:

        self._update_ranking_table()

        self._evaluate_absolute_score_credit()

        self._evaluate_ranking_shift()

        self.drop_sql_table(self._str_score_table_name)

    def check_sql_table_ranking_watch_list_is_quote_per_isin(self, str_isin: str) -> bool:

        str_text = (f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name} '

                    f'WHERE {self._str_ranking_watch_list_quote_isin_column_name} = "{str_isin}"')

        bool_result = False

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                tuple_result = self._my_sql_cursor.fetchone()

                if tuple_result is not None:
                    bool_result = True

                self._my_sql_connection.commit()


            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.check_sql_table_ranking_watch_list_is_quote_per_isin.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        return bool_result

    def get_ranking_watch_list_date_per_quote_isin(self, str_quote_isin: str) -> dict:

        _data = {}

        self._get_sql_table_ranking_watch_list_quote_per_isin(str_quote_isin)

        self._str_ranking_watch_list_quote_isin_value = str_quote_isin

        _data[self._str_ranking_watch_list_quote_isin_column_name] = self._str_ranking_watch_list_quote_isin_value
        _data[self._str_ranking_watch_list_analyst_score_column_name] = self._float_ranking_watch_list_analyst_score_value
        _data[self._str_ranking_watch_list_derivate_score_column_name] = self._float_ranking_watch_list_derivate_score_value
        _data[self._str_ranking_watch_list_fundamentals_score_column_name] = self._float_ranking_watch_list_fundamentals_score_value
        _data[self._str_ranking_watch_list_performance_score_column_name] = self._float_ranking_watch_list_performance_score_value
        _data[self._str_ranking_watch_list_overall_score_column_name] = self._float_ranking_watch_list_overall_score_value
        _data[self._str_ranking_watch_list_shift_column_name] = self._int_ranking_watch_list_shift_value

        return _data

    def calculate_mean_score_values(self) -> dict:

        _analyst: str = self._str_ranking_watch_list_analyst_score_column_name
        _derivate: str = self._str_ranking_watch_list_derivate_score_column_name
        _fundamentals: str = self._str_ranking_watch_list_fundamentals_score_column_name
        _performance: str = self._str_ranking_watch_list_performance_score_column_name
        _overall: str = self._str_ranking_watch_list_overall_score_column_name
        _str_table_name: str = self._str_table_name

        str_text: str = (f'SELECT '
                         f' AVG({_analyst}) AS mean_analyst, '
                         f' AVG({_derivate}) AS mean_derivate, '
                         f' AVG({_fundamentals}) AS mean_fundamentals, '
                         f' AVG({_performance}) AS mean_performance, '
                         f' AVG({_overall}) AS mean_overall '
                         f'FROM {_str_table_name} ')

        try:

            self._my_sql_cursor.execute(str_text)

            result = self._my_sql_cursor.fetchall()

            self._my_sql_connection.commit()

            result = [round(value, 2) for value in result[0]]

            keys = [self._str_ranking_watch_list_analyst_score_column_name,
                    self._str_ranking_watch_list_derivate_score_column_name,
                    self._str_ranking_watch_list_fundamentals_score_column_name,
                    self._str_ranking_watch_list_performance_score_column_name,
                    self._str_ranking_watch_list_overall_score_column_name]

            result = dict(zip(keys, result))

            return result

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.calculate_mean_score_values.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def query_top_ranking_close_earning_day(self) -> list[tuple]:

        _str_calendar_data_base_file_name: str = self._str_calendar_data_base_file_name
        _str_calendar_table_name: str = self._str_source_table_name_calendar
        _str_calendar_quote_isin: str = self._str_source_table_calendar_quote_isin_column_name
        _str_calendar_delta_earning_day: str = self._str_source_table_calendar_earnings_delta_date_column_name

        _str_ranking_table_name: str = self._str_table_name
        _str_ranking_quote_isin: str = self._str_ranking_watch_list_quote_isin_column_name
        _str_ranking_overall_score: str = self._str_ranking_watch_list_overall_score_column_name

        _str_static_table_name: str = self._str_source_table_name_static
        _str_static_quote_isin: str = self._str_source_table_static_quote_isin_column_name
        _str_static_quote_name: str = self._str_source_table_static_quote_name_column_name
        _str_static_quote_industry: str = self._str_source_table_static_quote_industry_column_name

        _str_fundamentals_table_name: str = myFundamentalsWatchListDefinitions.STR_DATA_BASE_TABLE_NAME
        _str_fundamentals_quote_isin: str = self._str_source_table_fundamentals_quote_isin_column_name
        _str_fundamentals_surprise_credit: str = self._str_source_table_fundamentals_surprise_credit_column_name

        list_result = []

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{_str_calendar_data_base_file_name}" AS db_calendar')

                # SQL-Abfrage ausführen
                _query = f"""
                                SELECT r.{_str_ranking_quote_isin}, s.{_str_static_quote_name}, s.{_str_static_quote_industry}, r.{_str_ranking_overall_score}, 
                                c.{_str_calendar_delta_earning_day}, f.{_str_fundamentals_surprise_credit}
                                FROM {_str_ranking_table_name} AS r
                                    JOIN db_calendar.{_str_calendar_table_name} AS c ON r.{_str_ranking_quote_isin} = c.{_str_calendar_quote_isin}
                                    JOIN {_str_fundamentals_table_name} AS f ON r.{_str_ranking_quote_isin} = f.{_str_fundamentals_quote_isin}
                                    JOIN {_str_static_table_name} AS s ON r.{_str_ranking_quote_isin} = s.{_str_static_quote_isin}
                                WHERE r.{_str_ranking_overall_score} > 1
                                AND c.{_str_calendar_delta_earning_day} BETWEEN -5 AND 20
                                ORDER BY c.{_str_calendar_delta_earning_day};
                            """

                self._my_sql_cursor.execute(_query)

                result = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

                if result.__len__() > 0:

                   list_result = result

            except sqlite3.OperationalError as err:

                print(f'---- Operational Error in {__title__}, {self.query_top_ranking_close_earning_day.__name__} ----, \n'
                      f'---- the Text {_query} has caused an Error {err} ! ----')

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_calendar')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

        return list_result

    def query_top_ranking_close_ex_dividend_day(self) -> list[tuple]:

        _str_calendar_data_base_file_name: str = self._str_calendar_data_base_file_name
        _str_calendar_table_name: str = self._str_source_table_name_calendar
        _str_calendar_quote_isin: str = self._str_source_table_calendar_quote_isin_column_name
        _str_calendar_ex_dividend_day: str = self._str_source_table_calendar_ex_dividend_delta_date_column_name

        _str_ranking_table_name: str = self._str_table_name
        _str_ranking_quote_isin: str = self._str_ranking_watch_list_quote_isin_column_name
        _str_ranking_overall_score: str = self._str_ranking_watch_list_overall_score_column_name

        _str_static_table_name: str = self._str_source_table_name_static
        _str_static_quote_isin: str = self._str_source_table_static_quote_isin_column_name
        _str_static_quote_name: str = self._str_source_table_static_quote_name_column_name
        _str_static_quote_industry: str = self._str_source_table_static_quote_industry_column_name

        _str_fundamentals_table_name: str = myFundamentalsWatchListDefinitions.STR_DATA_BASE_TABLE_NAME
        _str_fundamentals_quote_isin: str = self._str_source_table_fundamentals_quote_isin_column_name
        _str_fundamentals_ratio_dividend_yield: str = self._str_source_table_fundamentals_ratio_dividend_yield_column_name

        list_result = []

        if self._my_sql_connection and self._my_sql_cursor:

            try:
                # ATTACH ausführen
                self._my_sql_cursor.execute(
                    f'ATTACH DATABASE "{_str_calendar_data_base_file_name}" AS db_calendar')

                # SQL-Abfrage ausführen
                _query = f"""
                                SELECT r.{_str_ranking_quote_isin}, s.{_str_static_quote_name}, s.{_str_static_quote_industry}, r.{_str_ranking_overall_score}, 
                                c.{_str_calendar_ex_dividend_day}, f.{_str_fundamentals_ratio_dividend_yield}
                                FROM {_str_ranking_table_name} AS r
                                    JOIN db_calendar.{_str_calendar_table_name} AS c ON r.{_str_ranking_quote_isin} = c.{_str_calendar_quote_isin}
                                    JOIN {_str_fundamentals_table_name} AS f ON r.{_str_ranking_quote_isin} = f.{_str_fundamentals_quote_isin}
                                    JOIN {_str_static_table_name} AS s ON r.{_str_ranking_quote_isin} = s.{_str_static_quote_isin}
                                WHERE r.{_str_ranking_overall_score} > 1
                                AND c.{_str_calendar_ex_dividend_day} BETWEEN 1 AND 20
                                ORDER BY c.{_str_calendar_ex_dividend_day};
                            """

                self._my_sql_cursor.execute(_query)

                result = self._my_sql_cursor.fetchall()

                self._my_sql_connection.commit()

                if result.__len__() > 0:

                   list_result = result

            except sqlite3.OperationalError as err:

                print(f'---- Operational Error in {__title__}, {self.query_top_ranking_close_ex_dividend_day.__name__} ----, \n'
                      f'---- the Text {_query} has caused an Error {err} ! ----')

                exit(1)

            finally:
                # 6. DETACH im finally-Block garantiert, dass die DB sauber getrennt wird,
                # selbst wenn oben ein Fehler auftritt.
                try:

                    self._my_sql_cursor.execute('DETACH DATABASE db_calendar')

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError:

                    pass  # Verhindert Absturz, falls DETACH fehlschlägt, weil ATTACH schon fehlschlug

        return list_result



if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
