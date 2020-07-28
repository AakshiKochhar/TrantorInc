#!/usr/bin/env python
# coding: utf-8

# In[32]:


""" The following program will use Pandas to plot and get statistics from stock data."""
import datetime
import pandas
import pandas_datareader.data 
import matplotlib.pyplot
import matplotlib 
from pandas import Series, DataFrame
from matplotlib import style

# Will collect start till end date data.
initial_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime(2019, 12, 31)

# Will collect IBM's stock data.
dataframe = pandas_datareader.data.DataReader("AMZN", 'yahoo', initial_date, end_date) # preparing to call for Amazon stock data
dataframe.tail()


# In[33]:


# Calculates the 'roling average'.
closing_price = dataframe['Adj Close']
rolling_average = closing_price.rolling(window=40).mean()

get_ipython().run_line_magic('matplotlib', 'inline')

# Adjusts length and height of PLT. 
matplotlib.rc('figure', figsize=(8, 7))
matplotlib.__version__

# Creates the 'rolling average' graph.
style.use('ggplot')
closing_price.plot(label='Amazon')
rolling_average.plot(label='Rolling average')
matplotlib.pyplot.legend()


# In[27]:


# Compares IBM to its competitors.
dataframe_competition = pandas_datareader.data.DataReader(['AAPL', 'GOOGL', 'IBM', 'MSFT', 'AMZN', 'ORCL'],'yahoo',start=initial_date,end=end_date)['Adj Close']
dataframe_competition.tail() 


# In[28]:


returns_competition = dataframe_competition.pct_change()

corr = returns_competition.corr()


# In[29]:


# Plots comparison of return distributions between companies.
matplotlib.pyplot.scatter(returns_competition.AMZN, returns_competition.ORCL)
matplotlib.pyplot.ylabel('Returns Oracle')
matplotlib.pyplot.xlabel('Returns Amazon')


# In[ ]:




