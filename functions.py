
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
from ast import Return
import pandas as pd

class PublicTradesMeasures:

    def __init__(self, pt_data: pd.DataFrame) -> pd.DataFrame:
        self.pt_data = pt_data

    def transaction_volume(self, by: str) -> pd.Series:
        n_pt_data = self.pt_data['side'].resample(by).count()
        return n_pt_data
    
    def asset_volume(self, by: str) -> pd.Series:
        v_pt_data = self.pt_data['amount'].resample(by).sum()
        return v_pt_data

    def high_price(self, by: str) -> pd.Series:
        h_pt_data = self.pt_data['price'].resample(by).max()
        return h_pt_data
    
    def low_price(self, by: str) -> pd.Series:
        l_pt_data = self.pt_data['price'].resample(by).min()
        return l_pt_data

    def open_price(self, by: str) -> pd.Series:
        o_pt_data = self.pt_data['price'].resample(by).first()
        return o_pt_data

    def close_price(self, by: str) -> pd.Series:
        c_pt_data = self.pt_data['price'].resample(by).last()
        return c_pt_data
    
    def ohclvv(self, by: str) -> pd.DataFrame:
        ohclvv = pd.DataFrame({'Open price': self.open_price(by), 'High price': self.high_price(by), 
                       'Low price': self.low_price(by),'Close price': self.close_price(by),
                       'Asset Volume': self.asset_volume(by), 'Transaction Volume': self.transaction_volume(by)})
        return ohclvv

    def trade_flow_imbalance(self, by: str) -> pd.DataFrame:
        trade_flow_imbalance = pd.DataFrame(self.pt_data[self.pt_data['side'] == "buy"]['amount'].resample(by).sum() 
                               - self.pt_data[self.pt_data['side'] == "sell"]['amount'].resample(by).sum())
        return trade_flow_imbalance
