"""myRankkingWatchList.py."""

__title__: str = "myRankingWatchList"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
from typing import Optional
from mytuple import myTuple
from mydatabase import mySQLDataBase
from myfilebase import myFileBase
from mysharesdefinition import myRankingWatchListDefinitions
from mywatchlist import myTableSQLRankingWatchList


@dataclasses.dataclass(init=False)
class MyRankingWatchList(mySQLDataBase.MySQLDataBase):
    """

    """
    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # SQL Table Static Watch List
    _my_table_sql_ranking_watch_list: myTableSQLRankingWatchList.MyTableSQLRankingWatchList = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLRankingWatchList.MyTableSQLRankingWatchList)))

    # table data as list of dict from SQL Data Base


    def __init__(self, str_working_directory: Optional[str] = None,
                 str_data_base_filename: Optional[str] = None) -> None:
        super().__init__()

        # init myTuple
        self._index_tuple = myTuple.MyTuple

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        # init working directory for Data Base
        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

        else:

            self._my_file.set_directory(myRankingWatchListDefinitions.STR_DATA_BASE_DIR_NAME)

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(myRankingWatchListDefinitions.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myRankingWatchListDefinitions.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myRankingWatchListDefinitions.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self._my_table_sql_ranking_watch_list = myTableSQLRankingWatchList.MyTableSQLRankingWatchList(
            self._my_sql_connection,
            self._my_sql_cursor)

        self._list_column_names = self._my_table_sql_ranking_watch_list.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myRankingWatchListDefinitions.LIST_STATIC_WATCH_LIST_COLUMN_NAMES

        elif self._list_column_names.__len__() < len(
                myRankingWatchListDefinitions.LIST_STATIC_WATCH_LIST_COLUMN_NAMES):

            self._list_column_names = myRankingWatchListDefinitions.LIST_STATIC_WATCH_LIST_COLUMN_NAMES

        self._int_num_columns = self._list_column_names.__len__()

    def reset_ranking_watch_list(self) -> None:

        self._my_table_sql_ranking_watch_list.drop_sql_table()

        self._my_table_sql_ranking_watch_list.create_sql_data_base_table()

    def get_entire_data_base_file_name(self) -> str:

        return self._my_file.get_entire_file_name

    def get_table_column_names(self) -> list:

        return self._list_column_names

    def check_quote_in_watch_list(self, str_isin_number: str) -> bool:

        return self._my_table_sql_ranking_watch_list.check_sql_table_ranking_watch_list_is_quote_per_isin(
            str_isin_number)

    def evaluate_overall_credits(self) -> None:

        self._my_table_sql_ranking_watch_list.evaluate_overall_credits()

    def get_ranking_watch_list_data_per_quote_isin(self, str_quote_isin) -> dict:

        return self._my_table_sql_ranking_watch_list.get_ranking_watch_list_date_per_quote_isin(str_quote_isin)

    def calculate_mean_score_values(self) -> dict:

        return self._my_table_sql_ranking_watch_list.calculate_mean_score_values()

    def query_top_ranking_close_earning_day(self) -> list[dict]:

        return self._my_table_sql_ranking_watch_list.query_top_ranking_close_earning_day()

if __name__ == "__main__":
    myRanking = MyRankingWatchList('/Users/oliverrudow/PycharmProjects/Data', 'shares_data_base.db')
    print(myRanking.query_top_ranking_close_earning_day())