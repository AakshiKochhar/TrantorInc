#!/usr/bin/env python
# coding: utf-8

# In[304]:


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
dataframe = pandas_datareader.data.DataReader("IBM", 'yahoo', start, end) # preparing to call for IBM stock data
dataframe.tail()


# In[319]:


# Calculates the 'roling average'.
closing_price = df['Adj Close']
rolling_average = closing_price.rolling(window=40).mean()

get_ipython().run_line_magic('matplotlib', 'inline')

# Adjusts length and height of PLT. 
matplotlib.rc('figure', figsize=(8, 7))
matplotlib.__version__

# Creates the 'rolling average' graph.
style.use('ggplot')
closing_price.plot(label='IBM')
rolling_average.plot(label='Rolling average')
matplotlib.pyplot.legend()


# In[316]:


# Compares IBM to its competitors.
dataframe_competition = web.DataReader(['AAPL', 'GOOGL', 'IBM', 'MSFT', 'AMZN'],'yahoo',start=start,end=end)['Adj Close']
dataframe_competition.tail() 


# In[317]:


returns_competition = dataframe_competition.pct_change()

corr = returns_competition.corr()


# In[318]:


# Plots comparison of return distributions between companies.
matplotlib.pyplot.scatter(returns_competition.IBM, returns_competition.MSFT)
matplotlib.pyplot.ylabel('Returns Microsoft')
matplotlib.pyplot.xlabel('Returns IBM')


# In[ ]:




