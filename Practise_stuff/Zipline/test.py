
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from zipline.algorithm import TradingAlgorithm
from zipline.transforms import batch_transform
from zipline.utils.factory import load_from_yahoo
help(load_from_yahoo)