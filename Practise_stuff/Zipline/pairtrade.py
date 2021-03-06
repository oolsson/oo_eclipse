'''
Created on Apr 10, 2013

@author: samirvanza
'''
from datetime import datetime
#!/usr/bin/python
#
# Copyright 2013 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from zipline.algorithm import TradingAlgorithm
from zipline.transforms import batch_transform
from zipline.utils.factory import load_from_yahoo



@batch_transform
def ols_transform(data, sid1, sid2):
    """Computes regression coefficient (slope and intercept)
    via Ordinary Least Squares between two SIDs.
    """
    p0 = data.price[sid1]
    p1 = sm.add_constant(data.price[sid2])
    slope, intercept = sm.OLS(p0, p1).fit().params

    return slope, intercept


class Pairtrade(TradingAlgorithm):
    """Pairtrading relies on cointegration of two stocks.

    The expectation is that once the two stocks drifted apart
    (i.e. there is spread), they will eventually revert again. Thus,
    if we short the upward drifting stock and long the downward
    drifting stock (in short, we buy the spread) once the spread
    widened we can sell the spread with profit once they converged
    again. A nice property of this algorithm is that we enter the
    market in a neutral position.

    This specific algorithm tries to exploit the cointegration of
    XOMsi and Coca Cola by estimating the correlation between the
    two. Divergence of the spread is evaluated by z-scoring.
    """

    def initialize(self, window_length=100):
        self.spreads = []
        self.zscores = []
        self.invested = 0
        self.window_length = window_length
        self.ols_transform = ols_transform(refresh_period=self.window_length,
                                           window_length=self.window_length)

    def handle_data(self, data):
        ######################################################
        # 1. Compute regression coefficients between XOM and CVX
        params = self.ols_transform.handle_data(data, 'XOM', 'CVX')
        if params is None:
            return
        slope, intercept = params

        ######################################################
        # 2. Compute spread and zscore
        zscore = self.compute_zscore(data, slope, intercept)
        self.zscores.append(zscore)

        ######################################################
        # 3. Place orders
        self.place_orders(data, zscore)

    def compute_zscore(self, data, slope, intercept):
        """1. Compute the spread given slope and intercept.
           2. zscore the spread.
        """
        spread = (data['XOM'].price - (slope * data['CVX'].price + intercept))
        self.spreads.append(spread)
        spread_wind = self.spreads[-self.window_length:]
        zscore = (spread - np.mean(spread_wind)) / np.std(spread_wind)
        return zscore

    def place_orders(self, data, zscore):
        """Buy spread if zscore is > 2, sell if zscore < .5.
        """
        if zscore >= 2.0 and not self.invested:
            self.order('XOM', int(100 / data['XOM'].price))
            self.order('CVX', -int(100 / data['CVX'].price))
            self.invested = True
        elif zscore <= -2.0 and not self.invested:
            self.order('CVX', -int(100 / data['CVX'].price))
            self.order('XOM', int(100 / data['XOM'].price))
            self.invested = True
        elif abs(zscore) < .5 and self.invested:
            self.sell_spread()
            self.invested = False

    def sell_spread(self):
        """
        decrease exposure, regardless of position long/short.
        buy for a short position, sell for a long.
        """
        CVX_amount = self.portfolio.positions['CVX'].amount
        self.order('CVX', -1 * CVX_amount)
        XOM_amount = self.portfolio.positions['XOM'].amount
        self.order('XOM', -1 * XOM_amount)

if __name__ == '__main__':
    data = load_from_yahoo(stocks=['XOM', 'CVX'], start=datetime(2008,1,1), end=datetime(2012,1,1), indexes={})

    pairtrade = Pairtrade()
    results = pairtrade.run(data)
    data['spreads'] = np.nan
    data.spreads[pairtrade.window_length:] = pairtrade.spreads

    ax1 = plt.subplot(211)
    data[['XOM', 'CVX']].plot(ax=ax1)
    plt.ylabel('price')
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(212, sharex=ax1)
    data.spreads.plot(ax=ax2, color='r')
    plt.ylabel('spread')

    plt.show()