# Web-scrapes and plots a histogram of house prices in
# Ireland during a specified month
#
# Data obtained from: Property Services Regulatory Authority
# http://wwww.propertypriceregister.ie
#
# Author: Diana Morosan
# email: diana@codifydublin.com


import numpy as np
import matplotlib.pyplot as plt
import urllib2
import matplotlib as mpl

month1 = '01'
month2 = '02'
county = 'Dublin'

mpl.rc('font',family='Times New Roman', size = 18)
plt.figure(1,figsize=(13,9))

# 1

# plot month of interest
url = 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-2017-'+month1+'-'+county+'.csv/$FILE/PPR-2017-'+month1+'-'+county+'.csv'

response = urllib2.urlopen( url )
data = response.read()

data = list( data.split("\r\n") )

prices = []
for line in data[1:-1]: # first line is header
    l = line.split('\x80') # encoding of euro symbol - prices after symbol
    p = l[1].split(',')
    price = p[0] + p[1]
    prices.append(float(price[:-1])) # removing " at the end
    

max_price = np.max(prices)

plt.hist( prices, bins = 50, color = 'darkcyan', label = 'January' )
plt.grid(True)
plt.xlabel( 'Price (euro)')
plt.ylabel( 'Number of Houses')
plt.title( 'Prices of Houses Sold in Dublin')
ax = plt.gca()
ax.xaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))



# compare to a different month
url = 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-2017-'+month2+'-'+county+'.csv/$FILE/PPR-2017-'+month2+'-'+county+'.csv'

response = urllib2.urlopen( url )
data = response.read()

data = list( data.split("\r\n") )

prices = []
for line in data[1:-1]: # first line is header
    l = line.split('\x80') # encoding of euro symbol - prices after symbol
    p = l[1].split(',')
    price = p[0] + p[1]
    prices.append(float(price[:-1])) # removing " at the end


max_price = np.max(prices)

plt.hist( prices, bins = 50, histtype = 'step', color = 'lightcoral', linewidth = 5, label = 'February' )


plt.legend()
plt.show()


# Different ways to do this:

# 2
# Save to text file then analyse text file when needed
url = 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-2017-01-Dublin.csv/$FILE/PPR-2017-01-Dublin.csv'

file = urllib2.urlopen(url)
with open('test.txt','wb') as output:
    output.write(file.read())


# 3
# Read using pandas; some issues with encoding in Python 2.7 (euro symbol)
import pandas as pd

data = pd.read_csv(url)
price = data.columns[4]