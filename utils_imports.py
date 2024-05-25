import sys,os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import time
import numpy as np
import pandas as pd
import random as rn
from datetime import datetime

import statistics
from deap import base, creator, tools, algorithms

import palettable
import seaborn as sns
import matplotlib
from matplotlib import cm
from matplotlib import dates
from matplotlib import figure
from matplotlib import pyplot as plt
plt.rcParams['axes.unicode_minus'] = False


# import statsmodels.api as sm
# from statsmodels.tsa.arima.model import ARIMA

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)