"""myWatchListContainer.py."""

__title__: str = "myWatchListContainer"
__version__: str = "0.1.0"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
from typing import Optional
from mytuple import myTuple
from mywatchlist import myRankingWatchList, myReportTopList
from mystaticwatchlist import myStaticWatchList
from myanalystwatchlist import myAnalystWatchList
from myderivatewatchlist import myDerivateWatchList
from myfundamentalswatchlist import myFundamentalsWatchList
from myperformancewatchlist import myPerformanceWatchList
from mycalendarwatchlist import myCalendarWatchList
from mytimeseries import myTimeSeries
from myyfinance import myYFinance
from mysharesreport import myReport
from myfilebase import myFileBase

STR_WORKING_DIRECTORY: str = '/Users/oliverrudow/PycharmProjects/Data'

STR_CURRENT_DATA_BASE_FILE_NAME: str = 'shares_data_base.db'

STR_TIME_SERIES_DATA_BASE_DIR_NAME: str = 'time_series_data_base.db'

STR_TARGET_DIRECTORY_FOR_SAFETY_COPY: str = '/Users/oliverrudow/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/Data'

FLAG_SCAN_WATCHLIST: bool = True


@dataclasses.dataclass(init=False)
class MyWatchListContainer:
    """

    """
    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # Yahoo Finance App
    _my_y_finance: myYFinance.MyYFinance = dataclasses.field(init=False, default_factory=type(myYFinance.MyYFinance()))

    _str_working_directory: str = dataclasses.field(init=False, default_factory=str)

    _str_data_base_file_name: str = dataclasses.field(init=False, default_factory=str)

    _str_time_series_data_base_file_name: str = dataclasses.field(init=False, default_factory=str)

    _str_target_directory_for_safety_copy: str = dataclasses.field(init=False, default_factory=str)

    _my_static_watch_list: myStaticWatchList.MyStaticWatchList = (
        dataclasses.field(init=False, default_factory=type(myStaticWatchList.MyStaticWatchList)))

    _my_performance_watch_list: myPerformanceWatchList.MyPerformanceWatchList = (
        dataclasses.field(init=False, default_factory=type(myPerformanceWatchList.MyPerformanceWatchList)))

    _my_analyst_watch_list: myAnalystWatchList.MyAnalystWatchList = (
        dataclasses.field(init=False, default_factory=type(myAnalystWatchList.MyAnalystWatchList)))

    _my_calendar_watch_list: myCalendarWatchList.MyCalendarWatchList = (
        dataclasses.field(init=False, default_factory=type(myCalendarWatchList.MyCalendarWatchList)))

    _my_fundamentals_watch_list: myFundamentalsWatchList.MyFundamentalsWatchList = (
        dataclasses.field(init=False, default_factory=type(myFundamentalsWatchList.MyFundamentalsWatchList)))

    _my_derivate_watch_list: myDerivateWatchList.MyDerivateWatchList = (
        dataclasses.field(init=False, default_factory=type(myDerivateWatchList.MyDerivateWatchList)))

    _my_ranking_watch_list: myRankingWatchList.MyRankingWatchList = (
        dataclasses.field(init=False, default_factory=type(myRankingWatchList.MyRankingWatchList)))

    _my_time_series: myTimeSeries.MyTimeSeries = (
        dataclasses.field(init=False, default_factory=type(myTimeSeries.MyTimeSeries)))

    _my_report_top_list: myReportTopList.MyReportTopList = (
        dataclasses.field(init=False, default_factory=type(myReportTopList.MyReportTopList)))

    _my_report: myReport.MyReport = dataclasses.field(init=False, default_factory=type(myReport.MyReport))

    _num_quotes_in_static_watchlist: int = dataclasses.field(init=False, default=0)

    _flag_scan_watch_list: bool = dataclasses.field(init=False, default=FLAG_SCAN_WATCHLIST)


    def __init__(self,  str_working_directory: Optional[str] = None,
                 str_data_base_filename: Optional[str] = None,
                 flag_scan_watch_list: Optional[bool] = None) -> None:
        super().__init__()

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        # init myTuple
        self._index_tuple = myTuple.MyTuple

        # init y_finance
        self._my_y_finance = myYFinance.MyYFinance()

        # init scan flag
        if flag_scan_watch_list is not None:

            self._flag_scan_watch_list = flag_scan_watch_list

        else:

            self._flag_scan_watch_list = FLAG_SCAN_WATCHLIST

        # init working directory
        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

        else:

            self._my_file.set_directory(STR_WORKING_DIRECTORY)

        self._str_working_directory = self._my_file.get_directory_name

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(STR_CURRENT_DATA_BASE_FILE_NAME)

        self._str_data_base_file_name = self._my_file.get_file_name

        # init time series
        self._str_time_series_data_base_file_name = STR_TIME_SERIES_DATA_BASE_DIR_NAME

        # init safety copy
        self._str_target_directory_for_safety_copy = STR_TARGET_DIRECTORY_FOR_SAFETY_COPY

        self._my_file.set_target_directory_for_copy(self._str_target_directory_for_safety_copy)

        # init static_watch_list
        self._my_static_watch_list = myStaticWatchList.MyStaticWatchList(self._my_y_finance,
                                                                         self._str_working_directory,
                                                                         self._str_data_base_file_name)

        self._num_quotes_in_static_watchlist = self._my_static_watch_list.get_num_quotes_in_watch_list()

        # init performance watch list
        self._my_performance_watch_list = myPerformanceWatchList.MyPerformanceWatchList(self._my_y_finance,
                                                                            self._str_working_directory,
                                                                            self._str_data_base_file_name,
                                                                            self._flag_scan_watch_list)

        # init analyst watch list
        self._my_analyst_watch_list = myAnalystWatchList.MyAnalystWatchList(self._my_y_finance,
                                                                            self._str_working_directory,
                                                                            self._str_data_base_file_name)

        # init calendar watch list
        self._my_calendar_watch_list = myCalendarWatchList.MyCalendarWatchList(self._my_y_finance,
                                                                            self._str_working_directory,
                                                                            self._str_data_base_file_name)

        # init fundamentals watch list
        self._my_fundamentals_watch_list = myFundamentalsWatchList.MyFundamentalsWatchList(self._my_y_finance,
                                                                                        self._str_working_directory,
                                                                                        self._str_data_base_file_name)

        # init derivate watch list
        self._my_derivate_watch_list = myDerivateWatchList.MyDerivateWatchList(self._my_y_finance,
                                                                               self._str_working_directory,
                                                                               self._str_data_base_file_name)

        # init ranking watch list
        self._my_ranking_watch_list = myRankingWatchList.MyRankingWatchList(self._str_working_directory,
                                                                            self._str_data_base_file_name)

        # init report top list
        self._my_report_top_list = myReportTopList.MyReportTopList(self._str_working_directory,
                                                                    self._str_data_base_file_name)



        self._my_time_series = myTimeSeries.MyTimeSeries(self._str_working_directory,
                                                            self._str_time_series_data_base_file_name)

    def run_watchlist(self) -> None:

        if  self._flag_scan_watch_list:

            self.scan_watchlist()

        self.evaluate_data_base()

    def set_flag_scan_watch_list(self, flag: bool) -> None:

        self._flag_scan_watch_list = flag

    def close_watchlist(self) -> None:
        # Close Data Base
        self._my_static_watch_list.close_sql_data_base()

        self._my_performance_watch_list.close_sql_data_base()

        self._my_analyst_watch_list.close_sql_data_base()

        self._my_calendar_watch_list.close_sql_data_base()

        self._my_fundamentals_watch_list.close_sql_data_base()

        self._my_derivate_watch_list.close_sql_data_base()

        self._my_ranking_watch_list.close_sql_data_base()

        self._my_report_top_list.close_sql_data_base()

        self._my_time_series.close_time_series()

        self._my_time_series.close_sql_data_base()

        self._my_file.make_copy_from_file()

    def scan_watchlist(self)-> None:

        print(f'-----------------------------------------------------------------------------------------------------')
        print(f'---- the connected data base is: {self._my_static_watch_list.get_entire_data_base_file_name()} ')
        print(f'---- the number of quotes is: {self._num_quotes_in_static_watchlist} ')

        ind = 1

        self._my_performance_watch_list.reset_performance_watch_list()

        self._my_analyst_watch_list.reset_analyst_watch_list()

        self._my_calendar_watch_list.reset_calendar_watch_list()

        self._my_derivate_watch_list.reset_derivate_watch_list()

        self._my_fundamentals_watch_list.reset_fundamentals_watch_list()

        while ind < self._num_quotes_in_static_watchlist + 1:

            str_quote_isin = self._my_static_watch_list.get_next_quote_isin(ind)

            print(f'---- {ind}: {str_quote_isin}')

            self._my_y_finance.set_actual_quote_isin(str_quote_isin)

            self._my_y_finance.get_actual_quote_ticker_data_from_y_finance()

            self._my_performance_watch_list.get_performance_data_of_quote()

            self._my_analyst_watch_list.get_analyst_data_of_quote()

            self._my_calendar_watch_list.get_calendar_data_of_quote()

            self._my_fundamentals_watch_list.get_fundamentals_data_of_quote()

            self._my_derivate_watch_list.get_derivate_data_of_quote()

            ind += 1

    def evaluate_data_base(self)-> None:
        self._my_ranking_watch_list.reset_ranking_watch_list()

        self._my_report_top_list.reset_report_top_list()

        # Evaluate Data Base
        self._my_performance_watch_list.set_sectors_list(self._my_static_watch_list.get_list_sectors)

        self._my_performance_watch_list.set_industries_list(self._my_static_watch_list.get_list_industries)

        self._my_performance_watch_list.set_sectors_change_percent_score_list()

        self._my_performance_watch_list.evaluate_performance_credits()

        self._my_analyst_watch_list.evaluate_analyst_credits()

        self._my_derivate_watch_list.evaluate_derivate_credits()

        self._my_fundamentals_watch_list.evaluate_fundamentals_credits()

        self._my_ranking_watch_list.evaluate_overall_credits()

        self._my_calendar_watch_list.clean_calendar_data()

        self._my_time_series.update_sectors(self._my_static_watch_list.get_list_sectors)

        self._my_time_series.update_industries(self._my_static_watch_list.get_list_industries)

        self._my_time_series.update_sectors_change_percent(
            self._my_performance_watch_list.get_segmented_average_change_percent())

        self._my_time_series.update_industries_change_percent(
            self._my_performance_watch_list.get_industries_average_change_percent())

        self._my_time_series.update_scores()

        self._my_time_series.update_date()

        self._my_report_top_list.create_overall_report_tables()


if __name__ == "__main__":
    my_watch_list = MyWatchListContainer(None, None,True)
    my_watch_list.run_watchlist()
    my_watch_list.close_watchlist()

