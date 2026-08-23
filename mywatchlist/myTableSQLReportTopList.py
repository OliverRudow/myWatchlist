"""myTableSQLReportTopList.py."""

__title__: str = "myTableSQLReportTopList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import mySQLDataBase, myTableSQL
from mysharesdefinition import myRankingWatchListDefinitions, myPerformanceWatchListDefinitions, myReportTopListDefinitions, \
    myStaticWatchListDefinitions

INT_LIMIT_NUMBER_OF_SHARES_FROM_RANKING_WATCH_LIST: int = 23


@dataclasses.dataclass(init=False)
class MyTableSQLReportTopList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_report_top_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column names
    _str_report_top_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_quote_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_quote_industry_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_quote_currency_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_current_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_change_percent_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_change_percent_twenty_day_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_analyst_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_derivate_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_fundamentals_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_performance_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_twenty_day_change_percent_json_array_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_overall_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_report_top_list_shift_column_name: str = dataclasses.field(repr=False, default='')

    _int_number_of_shares_from_ranking_watch_list: int = dataclasses.field(repr=False, default=0)

    # ranking watch list column names
    _str_ranking_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_analyst_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_derivate_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_fundamentals_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_performance_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_overall_score_column_name: str = dataclasses.field(repr=False, default='')
    _str_ranking_watch_list_shift_column_name: str = dataclasses.field(repr=False, default='')

    # static watch list column names
    _str_static_watch_list_table_name: str = dataclasses.field(repr=False, default='')
    _str_static_watch_list_quote_name_column_name: str = dataclasses.field(repr=False, default='')
    _str_static_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_static_watch_list_quote_industry_column_name: str = dataclasses.field(repr=False, default='')
    _str_static_watch_list_quote_currency_column_name: str = dataclasses.field(repr=False, default='')

    # performance watch list column names
    _list_performance_watch_list_tables: list[str] = dataclasses.field(repr=False, default_factory=list)
    _str_performance_watch_list_table_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_table_name_twenty_day: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_current_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_change_percent_column_name: str = dataclasses.field(repr=False, default='')

    # performance credit watch list
    _str_performance_credit_table_name: str = dataclasses.field(repr=False, default='')
    _str_performance_credit_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_twenty_day_change_percent_json_object_column_name: str = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myReportTopListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_table_name(myReportTopListDefinitions.STR_DATA_BASE_TABLE_NAME)

        self._int_number_of_shares_from_ranking_watch_list = INT_LIMIT_NUMBER_OF_SHARES_FROM_RANKING_WATCH_LIST

        # column quote isin
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column quote name
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_NAME

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column quote industry
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_INDUSTRY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column quote currency
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_CURRENCY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column current price
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_CURRENT_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column change percent
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column change percent twenty day
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT_TWENTY_DAY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column analyst score
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_ANALYST_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column derivate score
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_DERIVATE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fundamentals score
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_FUNDAMENTALS_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column performance score
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_PERFORMANCE_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column twenty day change percent jason array
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column overall score
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_OVERALL_SCORE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column shift
        my_special_tuple = myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_SHIFT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check Watch exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_ISIN)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_report_top_list_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        self._init_ranking_watch_list_columns()

        self._init_static_watch_list_columns()

        self._init_performance_watch_list_columns()

    def _init_report_top_list_columns(self) -> None:

        self._str_report_top_list_quote_isin_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_ISIN)

        self._str_report_top_list_quote_name_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_NAME)

        self._str_report_top_list_quote_industry_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_INDUSTRY)

        self._str_report_top_list_quote_currency_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_QUOTE_CURRENCY)

        self._str_report_top_list_current_price_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_CURRENT_PRICE)

        self._str_report_top_list_change_percent_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT)

        self._str_report_top_list_change_percent_twenty_day_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_CHANGE_PERCENT_TWENTY_DAY)

        self._str_report_top_list_analyst_score_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_ANALYST_SCORE)

        self._str_report_top_list_derivate_score_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_DERIVATE_SCORE)

        self._str_report_top_list_fundamentals_score_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_FUNDAMENTALS_SCORE)

        self._str_report_top_list_performance_score_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_PERFORMANCE_SCORE)

        self._str_report_top_list_twenty_day_change_percent_json_array_credit_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_TWENTY_DAY_CHANGE_PERCENT_JSON_ARRAY)

        self._str_report_top_list_overall_score_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_OVERALL_SCORE)

        self._str_report_top_list_shift_column_name = self.get_column_name_from_dict(
            myReportTopListDefinitions.TUPLE_REPORT_TOP_LIST_SHIFT)

    def _init_ranking_watch_list_columns(self) -> None:

        self._str_ranking_watch_list_quote_isin_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_analyst_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_ANALYST_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_derivate_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_DERIVATE_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_fundamentals_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_FUNDAMENTALS_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_performance_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_PERFORMANCE_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_overall_score_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_OVERALL_SCORE[self._index_tuple.DATA_CONTENT][0])

        self._str_ranking_watch_list_shift_column_name = (
            myRankingWatchListDefinitions.TUPLE_RANKING_WATCH_LIST_SHIFT[self._index_tuple.DATA_CONTENT][0])

    def _init_static_watch_list_columns(self) -> None:

        self._str_static_watch_list_table_name = myStaticWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._str_static_watch_list_quote_name_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_NAME[self._index_tuple.DATA_CONTENT][0])

        self._str_static_watch_list_quote_isin_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_static_watch_list_quote_industry_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_INDUSTRY[self._index_tuple.DATA_CONTENT][0])

        self._str_static_watch_list_quote_currency_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_CURRENCY[self._index_tuple.DATA_CONTENT][0])

    def _init_performance_watch_list_columns(self) -> None:

        self._list_performance_watch_list_tables = self.get_sql_set_of_tables(
            myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME)

        if self._list_performance_watch_list_tables.__len__() > 0:

            self._str_performance_watch_list_table_name = self._list_performance_watch_list_tables[0]
            self._str_performance_watch_list_table_name_twenty_day = self._list_performance_watch_list_tables[-1]

        else:

            self._str_performance_watch_list_table_name = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME
            self._str_performance_watch_list_table_name_twenty_day = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._str_performance_watch_list_quote_isin_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_performance_watch_list_current_price_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE[self._index_tuple.DATA_CONTENT][0])

        self._str_performance_watch_list_change_percent_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT[self._index_tuple.DATA_CONTENT][0])

        self._str_performance_credit_table_name = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_EVAL_NAME

        self._str_performance_credit_quote_isin_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0])

        self._str_performance_watch_list_twenty_day_change_percent_json_object_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT[self._index_tuple.DATA_CONTENT][0])

    def _insert_data_from_ranking_watch_list(self) -> None:

        _str_source_table_name = myRankingWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name} '
                    f'({self._str_report_top_list_quote_isin_column_name}, '
                    f'{self._str_report_top_list_analyst_score_column_name}, '
                    f'{self._str_report_top_list_derivate_score_column_name}, '
                    f'{self._str_report_top_list_fundamentals_score_column_name}, '
                    f'{self._str_report_top_list_performance_score_column_name}, '
                    f'{self._str_report_top_list_overall_score_column_name}, '
                    f'{self._str_report_top_list_shift_column_name}) '
                    f'SELECT {self._str_ranking_watch_list_quote_isin_column_name}, '
                    f'{self._str_ranking_watch_list_analyst_score_column_name}, '
                    f'{self._str_ranking_watch_list_derivate_score_column_name}, '
                    f'{self._str_ranking_watch_list_fundamentals_score_column_name}, '
                    f'{self._str_ranking_watch_list_performance_score_column_name}, '
                    f'{self._str_ranking_watch_list_overall_score_column_name}, '
                    f'{self._str_ranking_watch_list_shift_column_name} '
                    f'FROM {_str_source_table_name} '
                    f'ORDER BY {self._str_ranking_watch_list_overall_score_column_name} DESC ')


        try:

            self._my_sql_cursor.execute("PRAGMA journal_mode=WAL;")

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._insert_data_from_ranking_watch_list.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _update_report_top_list_table(self) -> None:

        # update quote name
        self._update_data_from_source_watch_list(self._str_static_watch_list_table_name,
                                                 self._str_static_watch_list_quote_name_column_name,
                                                 self._str_static_watch_list_quote_isin_column_name,
                                                 self._str_report_top_list_quote_name_column_name)

        # update quote industry
        self._update_data_from_source_watch_list(self._str_static_watch_list_table_name,
                                                 self._str_static_watch_list_quote_industry_column_name,
                                                 self._str_static_watch_list_quote_isin_column_name,
                                                 self._str_report_top_list_quote_industry_column_name)

        # update quote currency
        self._update_data_from_source_watch_list(self._str_static_watch_list_table_name,
                                                 self._str_static_watch_list_quote_currency_column_name,
                                                 self._str_static_watch_list_quote_isin_column_name,
                                                 self._str_report_top_list_quote_currency_column_name)

        # update current price
        self._update_data_from_source_watch_list(self._str_performance_watch_list_table_name,
                                                 self._str_performance_watch_list_current_price_column_name,
                                                 self._str_performance_watch_list_quote_isin_column_name,
                                                 self._str_report_top_list_current_price_column_name)

        # update change percent
        self._update_data_from_source_watch_list(self._str_performance_watch_list_table_name,
                                                 self._str_performance_watch_list_change_percent_column_name,
                                                 self._str_performance_watch_list_quote_isin_column_name,
                                                 self._str_report_top_list_change_percent_column_name)

    def _update_data_from_source_watch_list(self, str_source_table_name: str,
                                           str_source_column_name: str,
                                           str_source_reference_column_name: str,
                                           str_target_column_name: str) -> None:

        _target_table: str = self._str_table_name
        _source_table: str = str_source_table_name
        _target_col: str = str_target_column_name
        _source_col: str = str_source_column_name
        _target_ref: str = self._str_report_top_list_quote_isin_column_name
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

    def _update_json_group_array_from_source_watch_list(self) -> None:

        _target_table: str = self._str_table_name
        _source_table: str = self._str_performance_credit_table_name
        _target_col: str = self._str_report_top_list_twenty_day_change_percent_json_array_credit_column_name
        _source_col: str = self._str_performance_watch_list_twenty_day_change_percent_json_object_column_name
        _target_ref: str = self._str_report_top_list_quote_isin_column_name
        _source_ref: str = self._str_performance_credit_quote_isin_column_name

        str_text = (
            f' UPDATE {_target_table} '
            f' SET {_target_col} = ( '
            f'      SELECT json_group_array(je.value) '
            f'      FROM {_source_table}, json_each({_source_table}.{_source_col}, "$.list") AS je '
            f'      WHERE {_source_table}.{_source_ref} = {_target_table}.{_target_ref} '
            f'      ORDER BY je.id'
            f' ) '
            f' WHERE EXISTS ('
            f'      SELECT 1 '
            f'      FROM {_source_table} '
            f'      WHERE {_source_table}.{_source_ref} = {_target_table}.{_target_ref} '
            f' )'
        )

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(
                f'---- Operational Error in {__title__}, {self._update_json_group_array_from_source_watch_list.__name__} ----, \n'
                f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _calculate_change_percent_twenty_days(self) -> None:

        _target_table: str = self._str_table_name
        _source_table: str = self._str_performance_watch_list_table_name_twenty_day
        _target_col: str = self._str_report_top_list_change_percent_twenty_day_column_name
        _target_ref: str = self._str_report_top_list_quote_isin_column_name
        _source_ref: str = self._str_performance_watch_list_quote_isin_column_name
        _source_col_twenty_day: str = self._str_performance_watch_list_current_price_column_name
        _source_col_today: str = self._str_report_top_list_current_price_column_name

        str_text = (
            f'UPDATE {_target_table} AS t '
            f'SET {_target_col} = ('
            f'  SELECT ROUND(CAST(t.{_source_col_today} - s.{_source_col_twenty_day} AS REAL) / s.{_source_col_twenty_day} * 100, 2) '
            f'  FROM {_source_table} AS s '
            f'  WHERE t.{_target_ref} = s.{_source_ref} '
            f'    AND t.{_source_col_today} IS NOT NULL '
            f'    AND s.{_source_col_twenty_day} IS NOT NULL '
            f'    AND s.{_source_col_twenty_day} <> 0'
            f') '
            f'WHERE EXISTS ('
            f'  SELECT 1 FROM {_source_table} AS s '
            f'  WHERE t.{_target_ref} = s.{_source_ref} '
            f'    AND t.{_source_col_today} IS NOT NULL '
            f'    AND s.{_source_col_twenty_day} IS NOT NULL '
            f'    AND s.{_source_col_twenty_day} <> 0'
            f')'
        )

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._calculate_change_percent_twenty_days.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def get_overall_score_report_data(self) -> list:

        _str_isin = self._str_report_top_list_quote_isin_column_name
        _str_name = self._str_report_top_list_quote_name_column_name
        _str_industry = self._str_report_top_list_quote_industry_column_name
        _str_curr = self._str_report_top_list_quote_currency_column_name
        _str_price = self._str_report_top_list_current_price_column_name
        _str_cp = self._str_report_top_list_change_percent_column_name
        _str_20d_cp = self._str_report_top_list_change_percent_twenty_day_column_name
        _str_a_sc = self._str_report_top_list_analyst_score_column_name
        _str_d_sc = self._str_report_top_list_derivate_score_column_name
        _str_f_sc = self._str_report_top_list_fundamentals_score_column_name
        _str_p_sc = self._str_report_top_list_performance_score_column_name
        _str_o_sc = self._str_report_top_list_overall_score_column_name
        _str_sh = self._str_report_top_list_shift_column_name

        _str_text = (f'SELECT '
                     f' {_str_isin}, '
                     f' {_str_name}, '
                     f' {_str_industry}, '
                     f' {_str_curr}, '
                     f' {_str_price}, '
                     f' {_str_cp}, '
                     f' {_str_20d_cp}, '
                     f' {_str_a_sc}, '
                     f' {_str_d_sc}, '
                     f' {_str_f_sc}, '
                     f' {_str_p_sc}, '
                     f' {_str_o_sc}, '
                     f' {_str_sh} '
                     f'FROM {self._str_table_name} '
                     f'ORDER BY {self._str_report_top_list_overall_score_column_name} DESC '
                     f'LIMIT {self._int_number_of_shares_from_ranking_watch_list}')

        try:

            self._my_sql_cursor.execute(_str_text)

            _data = self._my_sql_cursor.fetchall()

            _column_names = [description[0] for description in self._my_sql_cursor.description]

            self._my_sql_connection.commit()

            return _data

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_overall_score_report_data.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)

    def get_twenty_day_change_report_data(self) -> list:

        _str_isin = self._str_report_top_list_quote_isin_column_name
        _str_name = self._str_report_top_list_quote_name_column_name
        _str_industry = self._str_report_top_list_quote_industry_column_name
        _str_curr = self._str_report_top_list_quote_currency_column_name
        _str_price = self._str_report_top_list_current_price_column_name
        _str_cp = self._str_report_top_list_change_percent_column_name
        _str_20d_cp = self._str_report_top_list_change_percent_twenty_day_column_name
        _str_a_sc = self._str_report_top_list_analyst_score_column_name
        _str_d_sc = self._str_report_top_list_derivate_score_column_name
        _str_f_sc = self._str_report_top_list_fundamentals_score_column_name
        _str_p_sc = self._str_report_top_list_performance_score_column_name
        _str_o_sc = self._str_report_top_list_overall_score_column_name
        _str_sh = self._str_report_top_list_shift_column_name

        _str_text = (f'SELECT '
                     f' {_str_isin}, '
                     f' {_str_name}, '
                     f' {_str_industry}, '
                     f' {_str_curr}, '
                     f' {_str_price}, '
                     f' {_str_cp}, '
                     f' {_str_20d_cp}, '
                     f' {_str_a_sc}, '
                     f' {_str_d_sc}, '
                     f' {_str_f_sc}, '
                     f' {_str_p_sc}, '
                     f' {_str_o_sc}, '
                     f' {_str_sh} '
                     f'FROM {self._str_table_name} '
                     f'ORDER BY {self._str_report_top_list_change_percent_twenty_day_column_name} DESC '
                     f'LIMIT {self._int_number_of_shares_from_ranking_watch_list}')

        try:

            self._my_sql_cursor.execute(_str_text)

            _data = self._my_sql_cursor.fetchall()

            _column_names = [description[0] for description in self._my_sql_cursor.description]

            self._my_sql_connection.commit()

            return _data

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_twenty_day_change_report_data.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)

    def get_combined_overall_score_twenty_day_change_report_data(self) -> list:

        _str_isin = self._str_report_top_list_quote_isin_column_name
        _str_name = self._str_report_top_list_quote_name_column_name
        _str_industry = self._str_report_top_list_quote_industry_column_name
        _str_curr = self._str_report_top_list_quote_currency_column_name
        _str_price= self._str_report_top_list_current_price_column_name
        _str_cp = self._str_report_top_list_change_percent_column_name
        _str_20d_cp = self._str_report_top_list_change_percent_twenty_day_column_name
        _str_a_sc = self._str_report_top_list_analyst_score_column_name
        _str_d_sc = self._str_report_top_list_derivate_score_column_name
        _str_f_sc = self._str_report_top_list_fundamentals_score_column_name
        _str_p_sc = self._str_report_top_list_performance_score_column_name
        _str_o_sc = self._str_report_top_list_overall_score_column_name
        _str_sh = self._str_report_top_list_shift_column_name

        _str_text = (f'SELECT '
                     f' {_str_isin}, '
                     f' {_str_name}, '
                     f' {_str_industry}, '
                     f' {_str_curr}, '
                     f' {_str_price}, '
                     f' {_str_cp}, '
                     f' {_str_20d_cp}, '
                     f' {_str_a_sc}, '
                     f' {_str_d_sc}, '
                     f' {_str_f_sc}, '
                     f' {_str_p_sc}, '
                     f' {_str_o_sc}, '
                     f' {_str_sh} '
                     f'FROM {self._str_table_name} '
                     f'ORDER BY {self._str_report_top_list_overall_score_column_name} DESC, '
                     f'{self._str_report_top_list_change_percent_twenty_day_column_name} DESC '
                     f'LIMIT {self._int_number_of_shares_from_ranking_watch_list}')

        try:

            self._my_sql_cursor.execute(_str_text)

            _data = self._my_sql_cursor.fetchall()

            _column_names = [description[0] for description in self._my_sql_cursor.description]

            self._my_sql_connection.commit()

            return _data

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_combined_overall_score_twenty_day_change_report_data.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)

    def get_combined_overall_score_twenty_day_change_array(self) -> list:

        _str_isin = self._str_report_top_list_quote_isin_column_name
        _str_name = self._str_report_top_list_quote_name_column_name
        _str_industry = self._str_report_top_list_quote_industry_column_name
        _str_curr = self._str_report_top_list_quote_currency_column_name
        _str_price= self._str_report_top_list_current_price_column_name
        _str_cp = self._str_report_top_list_change_percent_column_name
        _str_20d_cp = self._str_report_top_list_change_percent_twenty_day_column_name
        _str_20d_cp_array = self._str_report_top_list_twenty_day_change_percent_json_array_credit_column_name
        _str_sh = self._str_report_top_list_shift_column_name

        _str_text = (f'SELECT '
                     f' {_str_isin}, '
                     f' {_str_name}, '
                     f' {_str_industry}, '
                     f' {_str_curr}, '
                     f' {_str_price}, '
                     f' {_str_cp}, '
                     f' {_str_20d_cp}, '
                     f' {_str_20d_cp_array}, '
                     f' {_str_sh} '
                     f'FROM {self._str_table_name} '
                     f'ORDER BY {self._str_report_top_list_overall_score_column_name} DESC, '
                     f'{self._str_report_top_list_change_percent_twenty_day_column_name} DESC '
                     f'LIMIT {self._int_number_of_shares_from_ranking_watch_list}')

        try:

            self._my_sql_cursor.execute(_str_text)

            _data = self._my_sql_cursor.fetchall()

            _column_names = [description[0] for description in self._my_sql_cursor.description]

            self._my_sql_connection.commit()

            return _data

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_combined_overall_score_twenty_day_change_array.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)


    def create_report_top_list(self) -> None:

        self._insert_data_from_ranking_watch_list()

        self._update_report_top_list_table()

        self._update_json_group_array_from_source_watch_list()

        self._calculate_change_percent_twenty_days()

if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
