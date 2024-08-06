from tabulate import tabulate
import pandas as pd
def tabulate_df(ds_nodash):
    year = ds_nodash[0:4]
    month = ds_nodash[4:6]
    read_df = pd.read_parquet(f'~/t2/test_parquet/ordered_parquet/year={year}/month={month}')
    headers = ['movieCd', 'movieNm', 'audiCnt', 'year', 'month']
    tabulate.WIDE_CHARS_MODE = False
    return read_df, tabulate(read_df, headers, tablefmt="rst")
