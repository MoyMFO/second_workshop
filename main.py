
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

from traceback import print_tb
import pandas as pd
import data as dt
from functions import PublicTradesMeasures



pt_data = dt.pt_data
data_1 = PublicTradesMeasures(pt_data=pt_data)

print(data_1.ohclvv(by='H'))

print(data_1.trade_flow_imbalance(by='H'))