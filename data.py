
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas as pd
import json
import numpy as np

pt_data = pd.read_csv('btcusdt_binance.csv', header=0)
# pt_data.drop('index', inplace=True, axis=1)

# Contar la cantidad de trades que ocurren cada hora
pt_data.index = pd.to_datetime(pt_data['timestamp'])
n_pt_data = pt_data['side'].resample('H').count()
v_pt_data = pt_data['amount'].resample('H').sum()
h_pt_data = pt_data['price'].resample('H').max()
l_pt_data = pt_data['price'].resample('H').min()
o_pt_data = pt_data.sort_index(ascending=True).iloc[0]['price']
c_pt_data = pt_data.sort_index(ascending=True).iloc[-1]['price']

# Seleccionar los renglones que tengan el index dentro de un rango definido de timestamps

rango_ts = []

# Crear un DF con los precios OHCLVV (Utilizar resample y algo tipo "fill")
# Cada Hora

OHCLVV = pd.DataFrame({'Operations Volume': n_pt_data, 'Volume': v_pt_data,
                       'High price': h_pt_data, 'Low price': l_pt_data,
                       'Open price': o_pt_data, 'Close price': c_pt_data})


# TradeFlow Imbalance:
# Cada Hora

# 4 momentos estadísticos oara las metricas Media, Varianza, Sesgo, Kurtosis