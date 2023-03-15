#####################################################
# Comparison of AB Test and Conversion of Bidding Methods
#####################################################

import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, ttest_ind

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

dataframe_control = pd.read_excel("./Desktop/ab_testing.xlsx" , sheet_name="Control Group")
dataframe_test = pd.read_excel("./Desktop/ab_testing.xlsx" , sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()

def check_df(dataframe, head=5):
    '''
    It is the function that looks at the overall picture with the given dataframe

    Parameters
    ----------
    dataframe: dataframe

    head : function of dataframe

    Returns
    -------
    '''

    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    
# df_control['Purchase'].mean() # 550.8940587702316
# df_test['Purchase'].mean() # 582.1060966484677

df_ = pd.concat([df_control.add_suffix('_control'),df_test.add_suffix('_test')], axis=1)
df = df_.copy()

######################################################

# H0: M1=M2 
# (There is no significant difference between M1 and M2.)

# H0: M1!=M2 
# (There is a significant difference between M1 and M2.)

######################################################

######################################################
# Normal Distribution
######################################################

# The argument H0 has a normal distribution could not be rejected with 95% confidence p-value > 0.05 

test_stat, pvalue = shapiro(df[['Purchase_test','Purchase_control']].dropna()) 
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

######################################################

######################################################
# Variance Distributions
######################################################

# The H0 variance distributions are homogeneous argument could not be rejected with 95% confidence. p-value >0.05

test_stat, pvalue = levene(df['Purchase_test'],
                           df['Purchase_control'])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
######################################################

######################################################
# Two Sample T test
######################################################

test_stat, pvalue = ttest_ind(df['Purchase_test'],
                               df['Purchase_control'],
                              equal_var=True)
######################################################

######################################################
# SUMMARY 

# Firstly, I used Shapiro wilks test for normality test, then I used Levene test for variance homogeneity. 
# My assumption checks were met and I could not reject either hypothesis. That's why I used a two-sample t-test.

