import pandas as pd
import numpy as np
#import scipy.stats as stats
from scipy.stats import mannwhitneyu

chat_id = 46951859 # Ваш chat ID, не меняйте название переменной

def solution(x,y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.01
    _,pv = stats.ttest_ind(x, y, equal_var=False)
    return pv < alpha
