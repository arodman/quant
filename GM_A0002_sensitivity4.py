
# coding: utf-8

# #aaa
# #a
# a
# 
# 
# 
# #Vix
# #Spx
# #Msci
# #Ust 
# #Ted spread, 
# #Dxy
# S#px volume
# #O##il price
# #C#ommoditi y idnex
# #Covid variantes????
# #2y, 10 year
# #10YEAR BREAKEVEN INFLATION OR 10Y REAL 
# #Copper
# #Nads,a ftse, dax, ted, srpe
# ###not only variaotns also volatiltiy  variacne stad deviaitons. 
# ###z score
# 

# In[ ]:


#IMPORT PACKAGES

import pandas as pd 
import os
from datetime import date
import datetime as dt
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
from pandas import DataFrame
#from statsmodels.regression.rolling import RollingOLS
import matplotlib.pyplot as plt
import numpy as np # numerical python
import seaborn as sns

#stacked
import tkinter
import matplotlib
matplotlib.use('TkAgg')


#import PILpi
#from PIL import Image
#import os
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileMerger
from datetime import datetime as dt


import statsmodels.api as sm
from scipy import stats
import numpy as np
from dateutil.relativedelta import relativedelta
import time


import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from pandas.plotting import table
import os
from datetime import date
import seaborn as sns
from random import seed
from random import random
import numpy as np
import PIL
from PIL import Image
#import os
from PyPDF2 import PdfFileMerger
from codetiming import Timer

import matplotlib.lines as mlines
from numpy.polynomial.polynomial import polyfit
import numpy
import scipy.stats

import scipy.stats


# In[ ]:


lst = ['BRL','COP','MXN','CLP','PEN','CZK','HUF','PLN','RUB','ILS','ZAR','TRY','IDR','THB','MYR','KRW','PHP']
lst2 = ['brazil','colombia','mexico','chile','peru','czech','hungary','poland','russia','israel','southafrica',
       'turkey','indonesia','thailand','malaysia','korea','philippines']
del lst 
del lst2


# * Load variables from sadbox

# In[ ]:


# y varaibles

#cds
#load data base and then create weekly variatons
cds_tmp = pd.read_csv (r'K:\2020_2431\q\sandbox_gm\cds_tmp.csv')
cds_tmp.rename(columns={'Date':'date'}, inplace=True)
#print(cds_tmp)
listx=(cds_tmp.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    cds_tmp[str("dv_"+variable)]= ((cds_tmp[str(variable)].diff()) /(cds_tmp[str(variable)].shift())).round(6)
    cds_tmp[str("dd_"+variable)]= ((cds_tmp[str(variable)].diff())).round(6)
    #print(cds_tmp[str("dv_"+variable)].head())
    #print(cds_tmp[str("dd_"+variable)].head())
    
     
cds_tmp=cds_tmp.fillna(method='ffill')    
cds_tmp=cds_tmp.fillna(method='bfill') 

data_y =cds_tmp 
print(data_y)   
del cds_tmp
del listx
print("Complete!!")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)



print("The type is : ",type(data_y["dv_cds5y_PEN"]))
print("The type is : ",type(data_y["dd_cds5y_PEN"]))


# In[ ]:


#read fx
fx_tmp= pd.read_csv (r'K:\2020_2431\q\sandbox_gm\fx_tmp.csv')
fx_tmp=fx_tmp.fillna(method='bfill')

####rename all columns
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::BRL CURNCY':'fx_BRL'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::CLP CURNCY':'fx_CLP'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::CNH CURNCY':'fx_CNH'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::COP CURNCY':'fx_COP'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::CZK CURNCY':'fx_CZK'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::IDR CURNCY':'fx_IDR'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::ILS CURNCY':'fx_ILS'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::INR CURNCY':'fx_INR'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::KRW CURNCY':'fx_KRW'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXN CURNCY':'fx_MXN'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::PEN CURNCY':'fx_PEN'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::PLN CURNCY':'fx_PLN'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::RUB CURNCY':'fx_RUB'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::HUF CURNCY':'fx_HUF'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::ZAR CURNCY':'fx_ZAR'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::THB CURNCY':'fx_THB'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::TWD CURNCY':'fx_TWD'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::MYR CURNCY':'fx_MYR'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::PHP CURNCY':'fx_PHP'}, inplace=True)
fx_tmp.rename(columns={'BBGTKR::BLOOMBERG::TRY CURNCY':'fx_TRY'}, inplace=True)


fx_tmp['fx_BRL']=pd.to_numeric(fx_tmp['fx_BRL'])
fx_tmp['fx_CLP']=pd.to_numeric(fx_tmp['fx_CLP'])
fx_tmp['fx_CNH']=pd.to_numeric(fx_tmp['fx_CNH'])
fx_tmp['fx_COP']=pd.to_numeric(fx_tmp['fx_COP'])
fx_tmp['fx_CZK']=pd.to_numeric(fx_tmp['fx_CZK'])
fx_tmp['fx_IDR']=pd.to_numeric(fx_tmp['fx_IDR'])
fx_tmp['fx_ILS']=pd.to_numeric(fx_tmp['fx_ILS'])
fx_tmp['fx_INR']=pd.to_numeric(fx_tmp['fx_INR'])
fx_tmp['fx_KRW']=pd.to_numeric(fx_tmp['fx_KRW'])
fx_tmp['fx_MXN']=pd.to_numeric(fx_tmp['fx_MXN'])
fx_tmp['fx_PEN']=pd.to_numeric(fx_tmp['fx_PEN'])
fx_tmp['fx_PLN']=pd.to_numeric(fx_tmp['fx_PLN'])
fx_tmp['fx_RUB']=pd.to_numeric(fx_tmp['fx_RUB'])
fx_tmp['fx_HUF']=pd.to_numeric(fx_tmp['fx_HUF'])
fx_tmp['fx_ZAR']=pd.to_numeric(fx_tmp['fx_ZAR'])
fx_tmp['fx_THB']=pd.to_numeric(fx_tmp['fx_THB'])
fx_tmp['fx_TWD']=pd.to_numeric(fx_tmp['fx_TWD'])
fx_tmp['fx_MYR']=pd.to_numeric(fx_tmp['fx_MYR'])
#fx_tmp['fx_PHP']=pd.to_numeric(fx_tmp['fx_PHP'])
fx_tmp['fx_TRY']=pd.to_numeric(fx_tmp['fx_TRY'])


fx_tmp['fx_BRL']=(fx_tmp['fx_BRL'])+0
fx_tmp['fx_CLP']=(fx_tmp['fx_CLP'])+0
fx_tmp['fx_CNH']=(fx_tmp['fx_CNH'])+0
fx_tmp['fx_COP']=(fx_tmp['fx_COP'])+0
fx_tmp['fx_CZK']=(fx_tmp['fx_CZK'])+0
fx_tmp['fx_IDR']=(fx_tmp['fx_IDR'])+0
fx_tmp['fx_ILS']=(fx_tmp['fx_ILS'])+0
fx_tmp['fx_INR']=(fx_tmp['fx_INR'])+0
fx_tmp['fx_KRW']=(fx_tmp['fx_KRW'])+0
fx_tmp['fx_MXN']=(fx_tmp['fx_MXN'])+0
fx_tmp['fx_PEN']=(fx_tmp['fx_PEN'])+0
fx_tmp['fx_PLN']=(fx_tmp['fx_PLN'])+0
fx_tmp['fx_RUB']=(fx_tmp['fx_RUB'])+0
fx_tmp['fx_HUF']=(fx_tmp['fx_HUF'])+0
fx_tmp['fx_ZAR']=(fx_tmp['fx_ZAR'])+0
fx_tmp['fx_THB']=(fx_tmp['fx_THB'])+0
fx_tmp['fx_TWD']=(fx_tmp['fx_TWD'])+0
fx_tmp['fx_MYR']=(fx_tmp['fx_MYR'])+0
#fx_tmp['fx_PHP']=pd.to_numeric(fx_tmp['fx_PHP'])
fx_tmp['fx_TRY']=(fx_tmp['fx_TRY'])+0




fx_tmp.rename(columns={'TIME':'date'}, inplace=True)
#fx_tmp['date'] = fx_tmp['date'].dt.strftime("%Y-%m-%d")
#fx_tmp['date'] = fx_tmp['date'].apply(lambda x: x.strftime("%Y-%m-%d"))
print(fx_tmp.columns)
print(fx_tmp.head())

listx=(fx_tmp.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    fx_tmp[str("dv_"+variable)]= ((fx_tmp[str(variable)].diff()) /(fx_tmp[str(variable)].shift())).round(6)
    fx_tmp[str("dd_"+variable)]= ((fx_tmp[str(variable)].diff())).round(6)
    print(fx_tmp[str("dv_"+variable)].head())
    print(fx_tmp[str("dd_"+variable)].head())
    
    
     
fx_tmp=fx_tmp.fillna(method='bfill') 
fx_tmp=fx_tmp.fillna(method='ffill') 
print(fx_tmp)
data_y=pd.merge(data_y, fx_tmp,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
del fx_tmp
del listx
#print(data_y)   

print("Complete")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)



print("The type is : ",type(data_y["dv_fx_ZAR"]))
print("The type is : ",type(data_y["dd_fx_ZAR"]))


# In[ ]:


#### local msci

l_msci_tmp= pd.read_csv (r'K:\2020_2431\q\sandbox_gm\l_msci_tmp.csv')
l_msci_tmp=l_msci_tmp.fillna(method='bfill')

####rename all columns
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXBR Index':'l_msci_BRL'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXCL Index':'l_msci_CLP'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXCN Index':'l_msci_CNH'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXCO Index':'l_msci_COP'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXCZ Index':'l_msci_CZK'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXID Index':'l_msci_IDR'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXIL Index':'l_msci_ILS'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXIN Index':'l_msci_INR'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXKR Index':'l_msci_KRW'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXMX Index':'l_msci_MXN'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXPE Index':'l_msci_PEN'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXPL Index':'l_msci_PLN'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXRU Index':'l_msci_RUB'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXHU Index':'l_msci_HUF'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXZA Index':'l_msci_ZAR'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXTH Index':'l_msci_THB'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::TAMSCI Index':'l_msci_TWD'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXMY Index':'l_msci_MYR'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::PHP CURNCY':'l_msci_PHP'}, inplace=True)
l_msci_tmp.rename(columns={'BBGTKR::BLOOMBERG::MXTR Index':'l_msci_TRY'}, inplace=True)


l_msci_tmp.rename(columns={'TIME':'date'}, inplace=True)
print(l_msci_tmp.columns)
print(l_msci_tmp.head())

listx=(l_msci_tmp.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    l_msci_tmp[str("dv_"+variable)]= ((l_msci_tmp[str(variable)].diff()) /(l_msci_tmp[str(variable)].shift())).round(6)
    l_msci_tmp[str("dd_"+variable)]= ((l_msci_tmp[str(variable)].diff())).round(6)
    print(l_msci_tmp[str("dv_"+variable)].head())
    print(l_msci_tmp[str("dd_"+variable)].head())
    
    
l_msci_tmp=l_msci_tmp.fillna(method='bfill')    
l_msci_tmp=l_msci_tmp.fillna(method='ffill') 
data_y=pd.merge(data_y, l_msci_tmp,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
del l_msci_tmp
del listx
print(data_y)  


print("Complete!!")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


######local ccy 10y 


### local msci

lccy_10y_tmp= pd.read_csv (r'K:\2020_2431\q\sandbox_gm\lccy_10y_tmp.csv')
lccy_10y_tmp=lccy_10y_tmp.fillna(method='bfill')

####rename all columns
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTILS10Y Govt':'lccy_ILS'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTZAR10Y Govt':'lccy_ZAR'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTHUF10Y Govt':'lccy_HUF'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTPEN10Y Govt':'lccy_PEN'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTCOP10Y Govt':'lccy_COP'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTBRL10Y Govt':'lccy_BRL'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTMYR10Y Govt':'lccy_MYR'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTPHP10Y Govt':'lccy_PHP'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTCNY10Y Govt':'lccy_CNY'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTIDR10Y Govt':'lccy_IDR'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTTHB10Y Govt':'lccy_THB'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTINR10Y Govt':'lccy_INR'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTTRY10Y Govt':'lccy_TRY'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTCZK10Y Govt':'lccy_CZK'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTPLN10Y Govt':'lccy_PLN'}, inplace=True)
lccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTMXN10Y Govt':'lccy_MXN'}, inplace=True)




lccy_10y_tmp.rename(columns={'TIME':'date'}, inplace=True)
print(lccy_10y_tmp.columns)
print(lccy_10y_tmp.head())

listx=(lccy_10y_tmp.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    lccy_10y_tmp[str("dv_"+variable)]= ((lccy_10y_tmp[str(variable)].diff()) /(lccy_10y_tmp[str(variable)].shift())).round(6)
    lccy_10y_tmp[str("dd_"+variable)]= ((lccy_10y_tmp[str(variable)].diff())).round(6)
    print(lccy_10y_tmp[str("dv_"+variable)].head())
    print(lccy_10y_tmp[str("dd_"+variable)].head())
    
    
lccy_10y_tmp=lccy_10y_tmp.fillna(method='bfill')    
lccy_10y_tmp=lccy_10y_tmp.fillna(method='ffill') 
data_y=pd.merge(data_y, lccy_10y_tmp,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
del lccy_10y_tmp
del listx
#print(data_y)  


print("Complete!!")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


##### hard currency 10y



hccy_10y_tmp= pd.read_csv (r'K:\2020_2431\q\sandbox_gm\hccy_10y_tmp.csv')
hccy_10y_tmp=hccy_10y_tmp.fillna(method='bfill')

####rename all columns

hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDBR10Y Govt':'hccy_BRL'}, inplace=True)
hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDCL10Y Govt':'hccy_CLP'}, inplace=True)
hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDMX10Y Govt':'hccy_MXN'}, inplace=True)
hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDID10Y Govt':'hccy_IDR'}, inplace=True)
hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDPE10Y Govt':'hccy_PEN'}, inplace=True)
hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDPH10Y Govt':'hccy_PHP'}, inplace=True)
hccy_10y_tmp.rename(columns={'BBGTKR::BLOOMBERG::GTUSDTR10Y Govt':'hccy_TRY'}, inplace=True)




hccy_10y_tmp.rename(columns={'TIME':'date'}, inplace=True)
print(hccy_10y_tmp.columns)
print(hccy_10y_tmp.head())

listx=(hccy_10y_tmp.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    hccy_10y_tmp[str("dv_"+variable)]= ((hccy_10y_tmp[str(variable)].diff()) /(hccy_10y_tmp[str(variable)].shift())).round(6)
    hccy_10y_tmp[str("dd_"+variable)]= ((hccy_10y_tmp[str(variable)].diff())).round(6)
    print(hccy_10y_tmp[str("dv_"+variable)].head())
    print(hccy_10y_tmp[str("dd_"+variable)].head())
    
    
hccy_10y_tmp=hccy_10y_tmp.fillna(method='bfill')    
hccy_10y_tmp=hccy_10y_tmp.fillna(method='ffill') 
data_y=pd.merge(data_y, hccy_10y_tmp,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
del hccy_10y_tmp
del listx
#print(data_y)  


print("Complete!!")


now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


# DATA X, INDEPENDENT VARIABLE, GLOBAL MACRO
datax = pd.read_csv (r'K:\2020_2431\q\sandbox_gm\datax_tmp.csv')
datax=datax.fillna(method='bfill')

datax.rename(columns={'TIME':'date'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGG10YR Index':'ust10y'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::MXUS INDEX':'msci_us'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::VIX INDEX':'vix'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::BASPTDSP Index':'ted'}, inplace=True)
#datax.rename(columns={'BBGTKR::BLOOMBERG::CO1 Comdty':'brent_oil'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::COA Comdty':'brent_oil'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::DAX Index':'dax'}, inplace=True)
#datax.rename(columns={'BBGTKR::BLOOMBERG::HG1 Comdty':'copper'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::HGA Comdty':'copper'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::MOODCAAA Index':'md_aaa'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::MOODCBAA Index':'md_baa'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::UKX Index':'ftse'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::US0003M Index':'libor3m'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGG2YR Index':'ust2y'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGG3M Index':'ust3m'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGG5YR Index':'ust5y'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGG7YR Index':'ust7y'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGGBE05 Index':'usbe5y'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::USGGBE10 Index':'usbe10y'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::XAG Curncy':'silver'}, inplace=True)
datax.rename(columns={'BBGTKR::BLOOMBERG::XAU Curncy':'gold'}, inplace=True)


datax['corp_spread']= (datax['md_baa'] - datax['md_aaa'] )
datax['ted_spread']= ((datax['libor3m'] - datax['ust3m'] )*100).round(6)

datax=datax.fillna(method='bfill')

listx=(datax.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    datax[str("dv_"+variable)]= ((datax[str(variable)].diff()) /(datax[str(variable)].shift())).round(6)
    datax[str("dd_"+variable)]= ((datax[str(variable)].diff())).round(6)
    print(datax[str("dv_"+variable)].head())
    print(datax[str("dd_"+variable)].head())
    
del  listx   
del  variable   
print('complete!!!') 
data_x=datax
del datax
data_x.to_csv (r'K:\2020_2431\q\sandbox_gm\data_x.csv', index = True, header=True)

#rnn_fin['corp_spread']= (rnn_fin['MOODCBAA Index'] - rnn_fin['MOODCAAA Index'] )
#rnn_fin['ted_spread']= ((rnn_fin['US0003M Index'] - rnn_fin['USGG3M Index'] )*100).round(6)

#####merge to aggregated dataset
#rnn_data=pd.merge(rnn_data, rnn_fin,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
#print(rnn_data)
print("Comeplte")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


#aaaaa


# In[ ]:


datac = pd.read_csv (r'K:\2020_2431\q\sandbox_gm\com_tmp.csv')
datac=datac.fillna(method='bfill')
datac.rename(columns={'TIME':'date'}, inplace=True)
datac.rename(columns={'BBGTKR::BLOOMBERG_PARENT::SPGSCI INDEX':'comm_index'}, inplace=True)
datac=datac.fillna(method='bfill')


listx=(datac.columns)
listx = listx[1:]
print(listx)

for x in range(len(listx)): 
    print(x)
    variable=str(listx[x])  
    print(variable)
    datac[str("dv_"+variable)]= ((datac[str(variable)].diff()) /(datac[str(variable)].shift())).round(6)
    datac[str("dd_"+variable)]= ((datac[str(variable)].diff())).round(6)
    
del  listx   
del  variable   
print('complete!!!') 
data_x=pd.merge(data_x, datac,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
data_x.to_clipboard()


# In[ ]:


#aaaa


# * COnsolidating datasets

# In[ ]:


#DATA Z MERGE both databases 
#merge bthh data x anbd data y
print(data_x.date)
print(data_y.date)

data_z=pd.merge(data_x, data_y,  how='left', left_on=['date'], right_on = ['date']).fillna(method='bfill')
data_z.to_csv (r'K:\2020_2431\q\sandbox_gm\data_z.csv', index = True, header=True)
print(data_z)
print("Complete!!!!")

del data_x
del data_y
#####

print("Comeplte")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


#* univariete regressions
#* view 1 year.----------. 
#* remind/// sensitivity,. 


# In[ ]:


#asdadsasdasdasd


# 
# # Global Macro Sensitivity analysis
# * Determine the sensitivty of each  security to important macro variables (linear regression models) and detect its magnitude over time
# 
# # Methodology
# * Linear regression of daily data points (EOD variation. No constant)
# 
# 
# # TIME DATA HORIZON MAKE REGRESISON (2011-2021/today) x10
# * time_ref00=2011-2021 ---last 10 years
# * time_ref01=2011-2019
# * time_ref02=2015-2019
# * time_ref03=2019-2020
# * time_ref04=2019-2021
# * time_ref05=2019
# * time_ref06=2020
# * time_ref07=2021
# * time_ref08=last 2 q
# * time_ref09=last 1 q
# 
# 
# # model x independent variables x10
# 
# * Vix [OK]
# * Spx [OK]
# * US 2 YEAR [OK]
# * US 5 YEAR [OK]
# * US 7 YEAR [OK]
# * US 10 YEAR [OK]
# * Ted spread,  [OK]
# * Dxy [OK]
# * Spx volume [OK]
# * Oil price [OK]
# * CommodiT idnex [OK]
# * Copper [OK]
# * Covid variants [OK]
# 
# 
# # model y dependnet variables x5
# 
# * Msci local [OK]
# * Fx local [OK]
# * Cds 5Y loca [OK]
# * 10y year local  [P]
# * 10Y hc  [P]
# 
# # Countries x30
# 
# * EM 
# * DM 
# 
# # Output x3
# 
# * coefficient regression
# * p_value
# * t_statistic
# 
# 
# # Results (Graphs)
# 
# * coefficient vs t statstics for each iteration country, varible x and variable y
# * coefficient vs t statstics inn one time horizon vs  coeff in other time horizon
# * coefficient vs t statstics of differente securities
# * compare sensitivity of one instrument country to two variables
# * ranking of more sensitive, only one varaibel. (coefciente bar plot)
# * for each country, its most significatgn sensisble
# * in a same graph the t and coefficient to differnet variables
# * plot all daily variations versus teh variable san run a line regressions (dot plot)
# * 1 unit odf standard deviaiton,  homonieigois translations
# 
# 

# In[ ]:


#GRAB
#MAKE LUIST OF THE INDEPENDENT VARIABLES
# GRAB LIOST
#dv_vix 
#dv_vix
#dv_msci_us

#Generalte correlaitns hsotircial, vs. what happened in the alst months. 
#Expected model ( from x to y dates), vs what happened last week. 
#SEE IF ITS ISIGNIFICATN, T STATISTIC. 

#DAILTY DATA



list_matrix = []
list_matrix0=['column_name',
              'type_horizon',
              'start',
              'end',
              'country',
              'variable_x',
              'type_variable_y',
              'variable_y',
              'coefficient',
              'p_value',
              't_statistic']

list_matrix = pd.Series(list_matrix0)       
list_matrix.columns = ["First"]
print(list_matrix)


# In[ ]:


#import datetime
Previous_Date = datetime.today() - timedelta(days=1)
Previous_Date=Previous_Date.strftime('%Y-%m-%d')
print (Previous_Date)


# In[ ]:


#time_ref00=2011-2021 ---last 10 years
#time_ref01=2011-2019
#time_ref02=2015-2019
#time_ref03=2019-2020
#time_ref04=2019-2021
#time_ref05=2019
#time_ref06=2020
#time_ref07=2021
#time_ref08=last 2 q
#time_ref09=last 1 q

start0 = '2019-01-01'
end0 = Previous_Date
start1 = '2020-01-01'
end1 = Previous_Date
start2 = '2021-01-01'
end2 = Previous_Date
start3 = datetime.today() - relativedelta(months=24) 
start3=start3.strftime('%Y-%m-%d')
#print(start6)
end3 = Previous_Date
start4 =  datetime.today() - relativedelta(months=12) 
start4=start4.strftime('%Y-%m-%d')
end4 = Previous_Date
start5 = datetime.today() - relativedelta(months=6) 
start5=start5.strftime('%Y-%m-%d')
end5 = Previous_Date
start6 = datetime.today() - relativedelta(months=3) 
start6=start6.strftime('%Y-%m-%d')
end6 = Previous_Date

#start0 = '2011-01-01'
#end0 = datetime.today().strftime('%Y-%m-%d')
#start1 = '2011-01-01'
#end1 = '2015-12-31'
#start2 = '2016-01-01'
#end2 = '2019-12-31'

#time_ref_list = ['0','1','2','3','4','5','6','7','8','9']
time_ref_list = ['0','1','2','3','4','5','6']
time_ref_start = [str(start0),str(start1),str(start2),str(start3),str(start4),str(start5),str(start6)]
time_ref_end   = [str(end0),str(end1),str(end2),str(end3),str(end4),str(end5),str(end6),]
time_horizon_name = []

#time_ref_start = [str(start0),str(start1),str(start2),str(start3),str(start4),
#                  str(start5),str(start6),str(start7),str(start8),str(start9)]
#time_ref_end = [str(end0),str(end1),str(end2),str(end3),str(end4),str(end5),
#                str(end6),str(end7),str(end8),str(end9),]


print(time_ref_start)
print(time_ref_end)
print("Comeplte")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


#x_list=['vix','msci_us','ust','dv_vix','dv_ust','dv_msci_us']
x_list=['ted_spread','brent_oil','dax','msci_us','ftse','libor3m',
        'ust10y','ust2y','ust3m','ust5y','ust7y','vix','silver',
        'gold','copper','corp_spread',
        'dv_ted_spread','dv_brent_oil','dv_dax','dv_msci_us','dv_ftse','dv_libor3m',
        'dv_ust10y','dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_vix','dv_silver',
        'dv_gold','dv_copper','dv_corp_spread']

###no copper acti
#MissingDataError: exog contains inf or nans

#y_list=['fx','cds5y','msci']
y_list=['dv_cds5y_','cds5y_','fx_','dv_fx_','l_msci_','dv_l_msci_','lccy_','dv_lccy_','hccy_','dv_hccy_']



country_list = ['BRL','COP','MXN','CLP','PEN','CZK','HUF','PLN','RUB','ILS','ZAR','TRY','IDR','THB','MYR','KRW']
#PHP
#country_list = ['brazil','colombia','mexico','chile','peru','czech','hungary','poland','russia','israel','southafrica',
#                'turkey','indonesia','thailand','malaysia','korea','philippines']



#filter_col = [col for col in data_z if col.startswith('dv_cds5y_')]
#filter_col
#loop_data_y=data_z[filter_col] 
#print(loop_data_y.columns)
#test = data_z.filter(like='korea').columns
#print(test)
print("Comeplte")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)



# # Loop
# * first loop is time window
# * second loop is determining x variables.
# * third loops is the specific Y variable. 
# * fourth loop is determining the country of analysis

# In[ ]:



###main looop witht eh t stacitists and coefficients. this takes hte most time


t0 = time.time()



list_matrix = []
list_matrix0=['column_name',
              'type_horizon',
              'start',
              'end',
              'country',
              'variable_x',
              'type_variable_y',
              'variable_y',
              'coefficient',
              'p_value',
              't_statistic',
              'correlation']

list_matrix = pd.Series(list_matrix0)       
list_matrix.columns = ["First"]
print(list_matrix)


n=0
for w in range(len(time_ref_start)): 
    print("time loop")
    print("w "+str(w))
    time_ref_list_n=str(time_ref_list[w])  
    time_ref_start_n=str(time_ref_start[w]) 
    time_ref_end_n=str(time_ref_end[w]) 
    loop_data = data_z[(data_z['date'] > str(time_ref_start_n)) & (data_z['date'] < str(time_ref_end_n))]
    print(n)
    #####filter time set here
    for x in range(len(x_list)): 
        print("x loop")
        print("x "+str(x))
        x_variable=str(x_list[x])
        loop_data_x=loop_data[[str(x_variable)]]
        print(n)
        ###fitlere variable here
        for y in range(len(y_list)): 
            ###fitlere variable here
            print("y loop")
            print("y "+str(y))
            y_variable=str(y_list[y])
            filter_col = [col for col in data_z if col.startswith(str(y_variable))]
            loop_data_y=loop_data[filter_col] 
            print(n)
            ###########selct coiutry and run regression
            for z in range(len(country_list)): 
                country_name=str(country_list[z])
                column_country=loop_data_y.filter(like=str(country_name)).columns
                
                if (len(column_country)+0)>0:
                    loop_data_y1=loop_data_y[column_country]           
                    endog=loop_data_y1
                    exog=loop_data_x
                    endog=endog.fillna(method='ffill') 
                    exog=exog.fillna(method='ffill') 
                    model = sm.OLS(endog.astype(float), exog.astype(float))
                    endog1=endog.astype(float)
                    exog1= exog.astype(float)
                    correlation_n = pd.concat([endog1, exog1], axis=1)
                    correlation_n=correlation_n.fillna(method='bfill') 
                    correlation_n = correlation_n.corr(method='pearson')
                    print(correlation_n)
                    correlation_n=correlation_n.iat[0, 1]
                    print(correlation_n)


                    rres = model.fit()  
                    name_x=str(loop_data_x.columns.values+"")
                    name_x=name_x.replace('[', '')
                    name_x=name_x.replace(']', '')
                    name_x=name_x.replace("'", '')
                    name_y=str(loop_data_y1.columns.values+"")
                    name_y=name_y.replace('[', '')
                    name_y=name_y.replace(']', '')
                    name_y=name_y.replace("'", '')
                    print("start here individual country loop")
                    print("w "+str(w))
                    print("x " +str(x))
                    print("y "+str(y))
                    print("z "+str(z))
                    print(time_ref_start_n)
                    print(time_ref_end_n)
                    print(x_variable)   
                    print(y_variable)
                    print(country_name)                
                    print(float(rres.params))
                    print(float(rres.pvalues))
                    print(float(rres.tvalues))
                    #print(rres.summary())
                    list2=[(str(name_y)+"_"+str(name_x)),
                           str(w),
                           str(time_ref_start_n),
                           str(time_ref_end_n),
                           str(country_name),
                           str(name_x),
                           str(y_variable),
                           str(name_y),
                           str(round(float(rres.params),10)),
                           str(round(float(rres.pvalues),10)),
                           str(round(float(rres.tvalues),10)),
                           str(correlation_n)]

                    list2 = pd.Series(list2)     
                    print(list2)  
                    list_matrix = pd.concat([list_matrix, list2], axis=1)
                    del list2
                    del country_name
                    del model
                    del rres
                    
                    
                else:
                    print("Empty element")
                    
                    
                    name_x=str(loop_data_x.columns.values+"")
                    name_x=name_x.replace('[', '')
                    name_x=name_x.replace(']', '')
                    name_x=name_x.replace("'", '')
                    name_y=str(loop_data_y1.columns.values+"")
                    name_y=name_y.replace('[', '')
                    name_y=name_y.replace(']', '')
                    name_y=name_y.replace("'", '')
                                      
                    list2=[(str(name_y)+"_"+str(name_x)),
                           str(w),
                           str(time_ref_start_n),
                           str(time_ref_end_n),
                           str(country_name),
                           str(name_x),
                           str(y_variable),
                           str(name_y),
                           str(0),
                           str(0),
                           str(0),
                           str(0)]

                    list2 = pd.Series(list2)     
                    print(list2)  
                    list_matrix = pd.concat([list_matrix, list2], axis=1)

                    del list2
                    del country_name

                    
                #print(list_matrix) 
                print("end individual country loop")
                n=n+1
                print(n)
    del time_ref_list_n
    del time_ref_start_n
    del time_ref_end_n
    del loop_data
    del loop_data_x
    del loop_data_y
    del loop_data_y1
    
    
    
print("Complete!!")        
t1 = time.time()
total = t1-t0
print("timer: "+str(total)+" seconds")             

#timer 276 seconds
#timer: 304.7816255092621 seconds
#timer: 513.6342921257019 seconds
#timer: 684.7583341598511 seconds
#timer: 738.2921142578125 seconds
#imer: 10446.21899485588 seconds

print("Comeplte")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


#print(len(list_matrix.columns))
#print(exog)
#print(endog)
#print(loop_data_x)
#print(loop_data_y)
#print(loop_data_y1)

#print(exog)
#print(country_name)
#print(column_country)
#print((len(column_country)+0))
#print((len(loop_data_y1)+0))
#len(loop_data_y1)


# In[ ]:


#### exmaple loop  
#    
#t0 = time.time()
#n=0
#for w in range(len(time_ref_start)):   
#    print("time loop")
#    print("w "+str(w))
#    time_ref_list_n=str(time_ref_list[w])  
#    time_ref_start_n=str(time_ref_start[w]) 
#    time_ref_end_n=str(time_ref_end[w])     
#    print(time_ref_list_n)
#    print(time_ref_start_n)
#    print(time_ref_end_n)
#    #####filter time set here
#    for x in range(len(x_list)): 
#        print("x loop")
#        print("x" +str(x))
#        x_variable=str(x_list[x])
#        print(x_variable)
#        ###fitlere variable here
#        for y in range(len(y_list)): 
#            print("y loop")
#            print("y "+str(y))
#            y_variable=str(y_list[y])
#            print(y_variable)
#            for z in range(len(country_list)):                
#                country_name=str(country_list[z])
#                print("start here individual country loop")
#                print("w "+str(w))
#                print("x " +str(x))
#                print("y "+str(y))
#                print("z "+str(z))
#                print(time_ref_start_n)
#                print(time_ref_end_n)
#                print(x_variable)   
#                print(y_variable)
#                print(country_name)                
#                print("end individual country loop")                
#                n=n+1
#                print(n)
#print("Complete!!")        
#t1 = time.time()
#total = t1-t0
#print("timer: "+str(total)+" seconds")


# In[ ]:


#Arrange format data
#list_matrix.head(10)
#print(list_matrix)
#list_matrix11 = list_matrix.set_index([])        
#print(list_matrix11)  

#new_header = df.iloc[0] #grab the first row for the header
list_matrix1 = list_matrix[1:] #take the data less the header row
list_matrix1.columns = list_matrix.iloc[0] 
list_matrix1 = list_matrix1.set_index(["column_name"])     
list_matrix1=list_matrix1.transpose()
list_matrix1.reset_index(level=0, inplace=True)
list_matrix1.rename(columns={list_matrix1.columns[0]: 'column_name1'}, inplace=True)
list_matrix1.drop_duplicates()

#data.rename(columns={'gdp':'log(gdp)'}, inplace=True)
#list_matrix1 = list_matrix1.apply(lambda r: sorted(r), axis = 1).drop_duplicates()
#list_matrix1.head(50)
#print(list_matrix1["country"])
#range_matrix=int(round(len(list_matrix1)/2,0))
#print(range_matrix)
#list_matrix1.drop(list_matrix1.index[-range_matrix])

print(len(list_matrix1))
list_matrix1=list_matrix1.dropna()  
list_matrix1 = list_matrix1[list_matrix1.t_statistic!= 'nan']
print(len(list_matrix1))

list_matrix1.to_csv (r'K:\2020_2431\q\sandbox_gm\matrix1_tmp.csv', index = True, header=True)
print("Complete!!")  
print(list_matrix1)
#35840
#35840


# In[ ]:


#del data_z
#del data_x
#del data_y
#del list_matrix1
#load data previos to startin the loop
list_matrix1 = pd.read_csv (r'K:\2020_2431\q\sandbox_gm\matrix1_tmp.csv')
print(list_matrix1.columns)


# * Matrix correlaiton table
# 

# In[ ]:


#table of correaltiosn of coeffcieintes
#first determine time hrozinos
#second determine filter the product
# frist group and one produc and idfferente time horizons, porduct x tmer hroizons. 


os.chdir('K:/2020_2431/q/gm_sensitivity/images/table/')

print(os.getcwd())


y_label= "Global Macro variables"
x_label= "EM Country"
variable_matrix='correlation'

parameter_label=10
parameter_tit=20
parameter_s1=20
parameter_s2=10

import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')



#'lccy_','dv_lccy_','hccy_','dv_hccy_']
#'lccy_','dv_lccy_','hccy_','dv_hccy_']
    
x0_list=['dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_ust10y',
        'dv_ted_spread','dv_corp_spread','dv_dax','dv_msci_us','dv_ftse','dv_vix',
        'dv_brent_oil_act','dv_gold','dv_silver','dv_copper',]

y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']
th=6
y_var = 'dv_l_msci_'
time_ref_list = ['0','1','2','3']


t0 = time.time()
 


n=0
for w in range(len(time_ref_list)): 
    print("time loop")
    #time_ref=str(time_ref_list[w+3])    
    time_ref_start_name=str(time_ref_start[w+3]) 
    time_ref_end_name=str(time_ref_end[w+3]) 
    time_ref_name=str(time_ref_start_name)+" / "+str(time_ref_end_name)
    th=w+3
    
    for y in range(len(y0_list)): 

        print("y loop")
        print("y "+str(y))
        y_var=str(y0_list[y])
        print(y_var)
        
        
        table_pv= list_matrix1
        table_pv=table_pv[table_pv.type_horizon==th]
        table_pv=table_pv[table_pv.type_variable_y==y_var]
        table_pv=table_pv[table_pv['variable_x'].str.contains("dv_")]
        table_pv=table_pv[['country','variable_x',str(variable_matrix)]]
        table_pv[str(variable_matrix)]=round(table_pv[str(variable_matrix)],2)
        print(len(table_pv))
        table_pv=pd.pivot_table(table_pv,index=["variable_x"],values=[str(variable_matrix)], columns=["country"],aggfunc=[np.sum])
        print(len(table_pv))
        table_pv.columns = table_pv.columns.get_level_values(2)
        table_pv = table_pv.reset_index()  
        table_pv=table_pv.set_index('variable_x')
        print(table_pv)


        #vmin=0
        #, vmax=1
        title_text0 ="GM - "+str(variable_matrix) 
        title_text1 =str(title_text0) +" table EM " + str(y_var) +"["+str(time_ref_name)+"]"
        x_label1=x_label+" "+str(y_var)


        plt.figure(figsize=(parameter_s1,parameter_s2))
        sns.heatmap(table_pv, cmap='RdYlGn', fmt="g",linewidths=0.6, annot=True)
        plt.ylabel(str(y_label), size=parameter_label)
        plt.xlabel(str(x_label1), size=parameter_label)
        plt.title(str(title_text1), size=parameter_tit)
        
        n=n+1
        print(n)
        
        plt.savefig(str(y_var)+"/table_"+str(y_var)+"th_"+str(th)+".pdf", bbox_inches='tight')
        plt.show()
        plt.close()
        plt.close('all')
        plt.clf()
        plt.cla()
print("Complete!!!!")
    
print("Complete!!")        
t1 = time.time()
total = t1-t0
print("timer: "+str(total)+" seconds")   

now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)
#timer: 101.14274072647095 seconds


# In[ ]:


source_dir= 'K:/2020_2431/q/gm_sensitivity/images/table/'
source_dir2= 'K:/2020_2431/q/gm_sensitivity/images/table/Summary/'
 

g0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']  
#g0_list=['dv_cds5y_','dv_fx_','dv_l_msci_']
#y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']

#####filter time set here
for x in range(len(g0_list)): 
        merger = PdfFileMerger()
        variable=str(g0_list[x])
        variable_folder = str(variable)+'/'
        source_dir1 = str(source_dir) + str(variable_folder) +"/"
        print(variable)
        print(source_dir1)
        for item in os.listdir(source_dir1):
             if item.endswith('pdf'):
                merger.append(source_dir1 + item)

        merger.write(source_dir2+variable+"_Complete.pdf") 
        #merger.write(public_location+variable+"_Complete.pdf")       
        merger.close()
        
        
        
        
print(table_pv)
print("Cmplete")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)
#timer: 101.14274072647095 seconds


# In[ ]:


#### Neww!!!! chart stacked bar chart with the correlation of 3 time hroizxons, ordere by the msot recents.  

#T:/Shared/XMJV/EM Asia Data/fx_data/
#loop
#table_pv=table_pv[table_pv.type_variable_y==y_var]
#os.chdir('K:/2020_2431/q/gm_sensitivity/images/table/')

os.chdir('K:/2020_2431/q/gm_sensitivity/images/correlation/')
print(os.getcwd())

y_label= "Global Macro variables"
x_label= "EM Country"
variable_matrix='correlation'

parameter_label=10
parameter_tit=20
parameter_s1=10
parameter_s2=10
parameter_y=10
parameter_x=10
parameter_z=10

parameter_f1=10
parameter_f2=10
parameter_t=8

import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
#6 3months
#5 is 6 motnhs
#4 is 12 months

print(list_matrix1)
t_corr=list_matrix1[list_matrix1.type_horizon>=4]
t_corr=t_corr[["country","variable_x","type_variable_y","type_horizon","correlation"]]
t_corr=t_corr[t_corr['type_variable_y'].str.contains("dv_")]
t_corr=t_corr[t_corr['variable_x'].str.contains("dv_")]
t_corr["correlation"]=round(t_corr["correlation"],2)
t_corr0=t_corr
######


#'lccy_','dv_lccy_','hccy_','dv_hccy_']
#'lccy_','dv_lccy_','hccy_','dv_hccy_']
#'dv_brent_oil_act'
x0_list=['dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_ust10y',
        'dv_ted_spread','dv_corp_spread','dv_dax','dv_msci_us','dv_ftse','dv_vix',
         'dv_gold','dv_silver','dv_copper',]

y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_']
#y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']



for x in range(len(x0_list)): 
    print("x loop")
    print("x "+str(x))
    variable_x_l=str(x0_list[x]) 
    print(variable_x_l)
    
    for y in range(len(y0_list)): 
        try:
            print("y loop")
            print("y "+str(y))
            type_variable_y_l=str(y0_list[y])
            print(type_variable_y_l)
            t_corr=t_corr0[t_corr0['variable_x'].str.contains(str(variable_x_l))]
            t_corr=t_corr[t_corr['type_variable_y'].str.contains(str(type_variable_y_l))]
            t_corr1=pd.pivot_table(t_corr,index=["country"],values=["correlation"], columns=["type_horizon"],aggfunc=[np.sum])
            t_corr1.columns = t_corr1.columns.get_level_values(2)
            t_corr1 = t_corr1.reset_index()
            t_corr1 = pd.DataFrame(t_corr1)
            print(t_corr1)
            #t_corr1 = t_corr1.set_index('country')
            t_corr2 = pd.DataFrame()
            t_corr2['country']=t_corr1['country']
            t_corr2['LAST YEAR']=t_corr1[t_corr1.columns[1]]
            t_corr2['LAST 6 MONTHS']=t_corr1[t_corr1.columns[2]]
            t_corr2['LAST 3 MONTHS']=t_corr1[t_corr1.columns[3]]
            print(t_corr1)
            print(t_corr2)
            graph_input=t_corr2
            chart=graph_input
            order_t=chart[['country','LAST 3 MONTHS']]
            order_t = order_t.sort_values(['LAST 3 MONTHS'], ascending=[False])
            order_t = order_t.reset_index()
            order_t = order_t.rename(columns={"index":"order"})
            order_t['order_1'] = (order_t.index + 1)*10
            del order_t['LAST 3 MONTHS']
            print(order_t)
            o_list=chart.columns 
            o_list = pd.DataFrame(o_list)
            o_list.columns=["order_sort"]
            o_list.drop(o_list.index[:1], inplace=True)
            o_list = o_list.reset_index()
            o_list = o_list.rename(columns={"index":"order"})
            o_list['order_2'] = (o_list.index )
            o_list['order_2'] = 5- o_list['order_2']
            print(o_list)

            z_title="Correlation "+str(variable_x_l)+"  "+str(type_variable_y_l)
            chart.set_index('country', inplace=True)
            df1 = chart.stack().reset_index().set_index('country').rename(columns={'level_1': 'Status', 0: 'Values'})
            df1 = df1.reset_index()
            print("look")
            print(df1)
            df1=pd.merge(df1, order_t[['country','order_1']],  how='left', left_on=['country'], right_on = ['country'])
            print(df1)
            print(o_list)
            print("look2")
            df1=pd.merge(df1, o_list[['order_sort','order_2']],  how='left', left_on=['Status'], right_on = ['order_sort']) 
            df1['order_3']=(df1['order_1']*df1['order_2'])

            df1 = df1.sort_values(['order_3'], ascending=[True])
            del df1['order_1']
            del df1['order_2']
            #be careful
            df1['Values']=(df1['Values']*1)
            print(df1)

            #graph specifics
            #large and height
            plt.figure(figsize=(parameter_f1,parameter_f2))
            sns.set_style('whitegrid')
            splot=sns.barplot(x='country', hue="Status", y="Values",
                                  palette=["darkorange", "lightsalmon","gray"], data=df1)
            plt.ylabel(y_label, size=parameter_y)
            plt.xlabel(x_label, size=parameter_x)
            plt.title(z_title, size=parameter_z)
            plt.tick_params(labelsize=parameter_t)

            plt.savefig(str(variable_x_l+"/correlation_"+variable_x_l+"_"+type_variable_y_l+".pdf"), bbox_inches='tight')
            plt.savefig(str("correlation_"+variable_x_l+"_"+type_variable_y_l+".pdf"), bbox_inches='tight')
            plt.close('all')
            plt.cla()   # Clear axis
            plt.clf()                          


            del t_corr
            del t_corr1
            del t_corr2
            del graph_input
            del o_list
            del order_t
            del df1
            del type_variable_y_l
        except KeyError:
            pass

print("COmplete")
print("Cmplete")
now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)
#timer: 101.14274072647095 seconds


# In[ ]:


######merge all pdfs
#'x_dv_libor3m'
g0_list=['dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_ust10y',
        'dv_ted_spread','dv_corp_spread','dv_dax','dv_msci_us','dv_ftse','dv_vix',
         'dv_gold','dv_silver','dv_copper',]


source_dir= 'K:/2020_2431/q/gm_sensitivity/images/correlation/'
source_dir2= 'K:/2020_2431/q/gm_sensitivity/images/correlation/pdf_x_dv/'
 
    
#####filter time set here
for x in range(len(g0_list)): 
        merger = PdfFileMerger()
        variable=str(g0_list[x])
        variable_folder = str(variable)+'/'
        source_dir1 = str(source_dir) + str(variable_folder)
        print(variable)
        
        for item in os.listdir(source_dir1):
             if item.endswith('pdf'):
                merger.append(source_dir1 + item)

        merger.write(source_dir2+variable+"_Complete.pdf") 
        #merger.write(public_location+variable+"_Complete.pdf")       
        merger.close()

        

now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)     


# #Create graphs 
# 
# * FIRST: coefficient vs t statstics for EACH TIME HORIZON, AND each VARIABLE Y iteration FOR country COUNTRY GROUP, varible x and variable y
# * SECOND: AGGREGATEING DIFFERENTE TIME HORIZON coefficient vs t statstics inn one time horizon vs  coeff in other time horizon
# * THIRD : SAME TIME HROIZON BUT DIFFERENT SECUTIRITES coefficient vs t statstics of differente securities. ALL INSTURMENTES AT THE SAME TIME
# * plot all daily variations versus teh variable san run a line regressions (dot plot)
# 
# * compare sensitivity of one instrument country to two variables
# * ranking of more sensitive, only one varaibel. (coefciente bar plot)
# * for each country, its most significatgn sensisble
# * in a same graph the t and coefficient to differnet variables
# 
# * 1 unit odf standard deviaiton,  homonieigois translations
# 

# In[ ]:


#First set

os.chdir('K:/2020_2431/q/gm_sensitivity/images/')
print(os.getcwd())

time_ref_list = ['0','1','2','3','4','5','6']

x0_list=['dv_libor3m','dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_ust10y',
        'dv_ted_spread','dv_corp_spread','dv_dax','dv_msci_us','dv_ftse','dv_vix',
        'dv_brent_oil_act','dv_gold','dv_silver','dv_copper',]

#y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_']
y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']


y_label="T_statistic"
x_label="Coefficient"
parameter_l=15
parameter_1=10
parameter_2=10


#inout tables
#list_matrix1



n=0
for w in range(len(time_ref_list)): 
    print("time loop")
    print("w "+str(w))
    time_ref_start_name=str(time_ref_start[w]) 
    time_ref_end_name=str(time_ref_end[w]) 
    time_ref_name=str(time_ref_start_name)+" / "+str(time_ref_end_name)

    #####filter time set here
    for x in range(len(x0_list)): 
        print("x loop")
        print("x "+str(x))
        x_variable=str(x0_list[x])
        print(x_variable)
        ###fitlere variable here
        for y in range(len(y0_list)): 
            ###fitlere variable here
            print("y loop")
            print("y "+str(y))
            y_variable=str(y0_list[y])
            print(y_variable)
         
            search_query = "variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable)+"' & type_horizon=='"+str(w)+"'"
            data_chart = list_matrix1.query(str(search_query))
            data_chart2=data_chart[['country','coefficient','t_statistic']]
            data_chart2["coefficient"] = pd.to_numeric(data_chart2["coefficient"])
            data_chart2["t_statistic"] = pd.to_numeric(data_chart2["t_statistic"])
            data_chart2["country"] = data_chart2["country"].astype(str)
            data_chart2["country1"] = data_chart2["country"]
            data_chart2["country1"] = data_chart2["country1"].astype('category')
            data_chart2 = data_chart2.copy()
            data_chart2.drop_duplicates()
            print(data_chart2)
            data_chart2.drop_duplicates()
            data_chart2["country"] = data_chart2["country"].astype(str)
            data_chart2.reset_index(drop=True)

            #print(data_chart2)
            print(n)
            n=n+1
                     
            
            df = data_chart2
            del data_chart2
            
            ###create lables
            time_ref_start_name=str(time_ref_start[w]) 
            time_ref_end_name=str(time_ref_end[w]) 
            time_ref_name=str(time_ref_start_name)+" / "+str(time_ref_end_name)
            
            # Data
            x = df["coefficient"]
            y = df["t_statistic"]
            labels = df["country1"]

            # Create the figure and axes objects
            fig, ax = plt.subplots(1, figsize=(10, 6))
            
            fig.suptitle("EM Global Macro Sensitivity Analysis: "+str(x_variable)+" vs. "+str(y_variable)+" Time: ("+str(time_ref_name)+")",size = 15)
            plt.title('Interpretation: t-stat ->  significance // reg coefficient -> sensitivity ', size=parameter_l)
            plt.ylabel(y_label, size=parameter_l)
            plt.xlabel(x_label, size=parameter_l)


            # Plot the scatter points
            ax.scatter(x, y,
                       color="blue",  # Color of the dots
                       s=100,         # Size of the dots
                       alpha=0.5,     # Alpha of the dots
                       linewidths=1)  # Size of edge around the dots

            # Add the participant names as text labels for each point
            for x_pos, y_pos, label in zip(x, y, labels):
                ax.annotate(label,             # The label for this point
                            xy=(x_pos, y_pos), # Position of the corresponding point
                            xytext=(7, 0),     # Offset text by 7 points to the right
                            textcoords='offset points', # tell it to use offset points
                            ha='left',         # Horizontally aligned to the left
                            va='center')       # Vertical alignment is centered

            plt.grid()
            ax.axhline(0, color='black', lw=1, alpha=0.75)
            ax.axvline(0, color='black', lw=1, alpha=0.75)
            # Show the plot
            n1=str(n)
            n1=n1.rjust(5, '0')
            plt.savefig((str(n1)+"_th"+str(w)+"_x_"+str(x_variable)+"_y_"+str(y_variable)+".jpg"), bbox_inches='tight')
            plt.savefig(("GM_reg_"+str(n1)+".jpg"), bbox_inches='tight')


print("Complete!!!!")

now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)



########
###IndexError: list index out of range


# In[ ]:


#print(data_chart2)

print(x_variable)
print(y_variable)

print(data_chart)
print(len(data_chart))
print("---")
print(data_chart2)
print(len(data_chart2))
print("---")
data_chart2["coefficient"] = (data_chart2["coefficient"]+0)


# In[ ]:


######aggregated time series
### 3 time series at the same time.



os.chdir('K:/2020_2431/q/gm_sensitivity/images/')
print(os.getcwd())

time_ref_list = ['0','1','2','3','4','5','6']

x0_list=['dv_libor3m','dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_ust10y',
        'dv_ted_spread','dv_corp_spread','dv_dax','dv_msci_us','dv_ftse','dv_vix',
        'dv_brent_oil_act','dv_gold','dv_silver','dv_copper',]

#y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_']
y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']


y_label="T_statistic"
x_label="Coefficient"
parameter_l=15
parameter_1=10
parameter_2=10


n=0
w1=4
w2=5
w3=6

t0 = time.time()


#####filter time set here
for x in range(len(x0_list)): 
        print("x loop")
        print("x "+str(x))
        x_variable=str(x0_list[x])

        ###fitlere variable here
        for y in range(len(y0_list)): 
            ###fitlere variable here
            print("y loop")
            print("y "+str(y))
            y_variable=str(y0_list[y])
         
            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable)+"' & type_horizon=='"+str(w1)+"'")
            data_chart1 = list_matrix1.query(str(search_query))
            data_chart1=data_chart1[['country','type_horizon','coefficient','t_statistic']]
            data_chart1["coefficient"] = pd.to_numeric(data_chart1["coefficient"])
            data_chart1["t_statistic"] = pd.to_numeric(data_chart1["t_statistic"])
            data_chart1["country"] = data_chart1["country"].astype(str)
            data_chart1["country1"] = data_chart1["country"]
            data_chart1["country1"] = data_chart1["country1"].astype('category')
            data_chart1 = data_chart1.copy()
            data_chart1.drop_duplicates()
            print(data_chart1)
            data_chart1.drop_duplicates()
            data_chart1["country"] = data_chart1["country"].astype(str)
            data_chart1.reset_index(drop=True)

            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable)+"' & type_horizon=='"+str(w2)+"'")
            data_chart2 = list_matrix1.query(str(search_query))
            data_chart2=data_chart2[['country','type_horizon','coefficient','t_statistic']]
            data_chart2["coefficient"] = pd.to_numeric(data_chart2["coefficient"])
            data_chart2["t_statistic"] = pd.to_numeric(data_chart2["t_statistic"])
            data_chart2["country"] = data_chart2["country"].astype(str)
            data_chart2["country1"] = data_chart2["country"]
            data_chart2["country1"] = data_chart2["country1"].astype('category')
            data_chart2 = data_chart2.copy()
            data_chart2.drop_duplicates()
            print(data_chart2)
            data_chart2.drop_duplicates()
            data_chart2["country"] = data_chart2["country"].astype(str)
            data_chart2.reset_index(drop=True)

            
            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable)+"' & type_horizon=='"+str(w3)+"'")
            data_chart3 = list_matrix1.query(str(search_query))
            data_chart3=data_chart3[['country','type_horizon','coefficient','t_statistic']]
            data_chart3["coefficient"] = pd.to_numeric(data_chart3["coefficient"])
            data_chart3["t_statistic"] = pd.to_numeric(data_chart3["t_statistic"])
            data_chart3["country"] = data_chart3["country"].astype(str)
            data_chart3["country1"] = data_chart3["country"]
            data_chart3["country1"] = data_chart3["country1"].astype('category')
            data_chart3 = data_chart3.copy()
            data_chart3.drop_duplicates()
            print(data_chart3)
            data_chart3.drop_duplicates()
            data_chart3["country"] = data_chart3["country"].astype(str)
            data_chart3.reset_index(drop=True)
            
            
            #print(data_chart2)
            print(n)
            n=n+1
                     
            
            df1 = data_chart1
            df2 = data_chart2
            df3 = data_chart3
            
            del data_chart1
            del data_chart2
            del data_chart3
            
            ###create lables
            time_ref_start_name1=str(time_ref_start[w1]) 
            time_ref_end_name1=str(time_ref_end[w1]) 
            time_ref_name1=str(time_ref_start_name1)+" / "+str(time_ref_end_name1)
            time_ref_start_name2=str(time_ref_start[w2]) 
            time_ref_end_name2=str(time_ref_end[w2]) 
            time_ref_name2=str(time_ref_start_name2)+" / "+str(time_ref_end_name2)
            time_ref_start_name3=str(time_ref_start[w3]) 
            time_ref_end_name3=str(time_ref_end[w3]) 
            time_ref_name3=str(time_ref_start_name3)+" / "+str(time_ref_end_name3)
            
            
            # Data
            x1 = df1["coefficient"]
            y1 = df1["t_statistic"]
            x2 = df2["coefficient"]
            y2 = df2["t_statistic"]
            x3 = df3["coefficient"]
            y3 = df3["t_statistic"]
            labels1 = df1["country1"]
            labels2 = df2["country1"]
            labels3 = df3["country1"]
            
            # Create the figure and axes objects
            fig, ax = plt.subplots(1, figsize=(10, 6))
            
            fig.suptitle("EM Global Macro Sensitivity Analysis: "+str(x_variable)+" vs. "+str(y_variable),size = 15)
            plt.title('Interpretation: t-stat ->  significance // reg coefficient -> sensitivity ', size=parameter_l)
            plt.ylabel(y_label, size=parameter_l)
            plt.xlabel(x_label, size=parameter_l)


            # Plot the scatter points
            ax.scatter(x1, y1,color="blue",s=100,alpha=0.5, linewidths=1,label=("Blue: ["+str(time_ref_name1)+"]"))  # Size of edge around the dots
            ax.scatter(x2, y2,color="red",s=100,alpha=0.5, linewidths=1,label=("Red: ["+str(time_ref_name2)+"]"))
            ax.scatter(x3, y3,color="green",s=100,alpha=0.5, linewidths=1,label=("Green: ["+str(time_ref_name3)+"]"))
            
            # Add the participant names as text labels for each point
            for x1_pos, y1_pos, label1 in zip(x1, y1, labels1):
                ax.annotate(label1,             # The label for this point
                            xy=(x1_pos, y1_pos), # Position of the corresponding point
                            xytext=(7, 0),     # Offset text by 7 points to the right
                            textcoords='offset points', # tell it to use offset points
                            ha='left',         # Horizontally aligned to the left
                            va='center')       # Vertical alignment is centered
            
            for x2_pos, y2_pos, label2 in zip(x2, y2, labels2):
                ax.annotate(label2,             # The label for this point
                            xy=(x2_pos, y2_pos), # Position of the corresponding point
                            xytext=(7, 0),     # Offset text by 7 points to the right
                            textcoords='offset points', # tell it to use offset points
                            ha='left',         # Horizontally aligned to the left
                            va='center') 
                
            for x3_pos, y3_pos, label3 in zip(x3, y3, labels3):
                ax.annotate(label3,             # The label for this point
                            xy=(x3_pos, y3_pos), # Position of the corresponding point
                            xytext=(7, 0),     # Offset text by 7 points to the right
                            textcoords='offset points', # tell it to use offset points
                            ha='left',         # Horizontally aligned to the left
                            va='center') 
                
                
            ax.legend(loc="lower right",title="Regression Time Horizons")    
            plt.grid()
            ax.axhline(0, color='black', lw=1, alpha=0.75)
            ax.axvline(0, color='black', lw=1, alpha=0.75)
            # Show the plot
            n1=str(n)
            n1=n1.rjust(5, '0')
            plt.savefig(("GM_agg_"+str(n1)+"x_"+str(x_variable)+"_y_"+str(y_variable)+".jpg"), bbox_inches='tight')
            plt.savefig(("x_"+str(x_variable)+"/GM_agg_"+str(n1)+"x_"+str(x_variable)+"_y_"+str(y_variable)+".pdf"), bbox_inches='tight')
            plt.savefig(("GM_agg_"+str(n1)+".jpg"), bbox_inches='tight')


print("Complete!!!!")


    
print("Complete!!")        
t1 = time.time()
total = t1-t0
print("timer: "+str(total)+" seconds")   


now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


######merge all pdfs
#'x_dv_libor3m'
g0_list=['x_dv_ust2y','x_dv_ust3m','x_dv_ust5y','x_dv_ust7y','x_dv_ust10y',
        'x_dv_ted_spread','x_dv_corp_spread','x_dv_dax','x_dv_msci_us','x_dv_ftse','x_dv_vix',
        'x_dv_brent_oil','x_dv_gold','x_dv_silver','x_dv_copper',]


source_dir= 'K:/2020_2431/q/gm_sensitivity/images/'
source_dir2= 'K:/2020_2431/q/gm_sensitivity/images/pdf_x_dv/'
 
    
#####filter time set here
for x in range(len(g0_list)): 
        merger = PdfFileMerger()
        variable=str(g0_list[x])
        variable_folder = str(variable)+'/'
        source_dir1 = str(source_dir) + str(variable_folder)
        print(variable)
        
        for item in os.listdir(source_dir1):
             if item.endswith('pdf'):
                merger.append(source_dir1 + item)

        merger.write(source_dir2+variable+"_Complete.pdf") 
        #merger.write(public_location+variable+"_Complete.pdf")       
        merger.close()

        

now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)        


# In[ ]:




os.chdir('K:/2020_2431/q/gm_sensitivity/images/')
print(os.getcwd())

#'dv_libor3m',

x0_list=['dv_ust2y','dv_ust3m','dv_ust5y','dv_ust7y','dv_ust10y',
        'dv_ted_spread','dv_corp_spread','dv_dax','dv_msci_us','dv_ftse','dv_vix',
        'dv_brent_oil','dv_gold','dv_silver','dv_copper',]

#y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_']
y0_list=['dv_cds5y_','dv_fx_','dv_l_msci_','dv_lccy_','dv_hccy_']

y_label="T_statistic"
x_label="Coefficient"
parameter_l=15
parameter_1=10
parameter_2=10

parameter_s1=20
parameter_s2=15

y_variable1= 'dv_cds5y_'
y_variable2= 'dv_fx_'
y_variable3= 'dv_l_msci_'
y_variable4= 'dv_lccy_'
y_variable5= 'dv_hccy_'


t0 = time.time()


n=0
#time_list = ['4','5','6']
time_list = ['4']

for w in range(len(time_list)): 
    print("time loop")
    print("w "+str(w))
    time_ref=(time_list[w]) 
    
    print(time_ref)
    time_ref_start_name=str(time_ref_start[(w+4)]) 
    time_ref_end_name=(time_ref_end[(w+4)]) 
    time_ref_name=str(time_ref_start_name)+" / "+str(time_ref_end_name)
    


    #####filter time set here
    for x in range(len(x0_list)): 
            print("x loop")
            print("x "+str(x))
            x_variable=str(x0_list[x])


            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable1)+"' & type_horizon=='"+str(time_ref)+"'")
            data_chart1 = list_matrix1.query(str(search_query))
            data_chart1=data_chart1[['country','type_horizon','coefficient','t_statistic']]
            data_chart1["coefficient"] = pd.to_numeric(data_chart1["coefficient"])
            data_chart1["t_statistic"] = pd.to_numeric(data_chart1["t_statistic"])
            data_chart1["country"] = data_chart1["country"].astype(str)
            data_chart1["country1"] = data_chart1["country"]
            data_chart1["country1"] = data_chart1["country1"].astype('category')
            data_chart1 = data_chart1.copy()
            data_chart1.drop_duplicates()
            print(data_chart1)
            data_chart1.drop_duplicates()
            data_chart1["country"] = data_chart1["country"].astype(str)
            data_chart1.reset_index(drop=True)

            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable2)+"' & type_horizon=='"+str(time_ref)+"'")
            data_chart2 = list_matrix1.query(str(search_query))
            data_chart2=data_chart2[['country','type_horizon','coefficient','t_statistic']]
            data_chart2["coefficient"] = pd.to_numeric(data_chart2["coefficient"])
            data_chart2["t_statistic"] = pd.to_numeric(data_chart2["t_statistic"])
            data_chart2["country"] = data_chart2["country"].astype(str)
            data_chart2["country1"] = data_chart2["country"]
            data_chart2["country1"] = data_chart2["country1"].astype('category')
            data_chart2 = data_chart2.copy()
            data_chart2.drop_duplicates()
            print(data_chart2)
            data_chart2.drop_duplicates()
            data_chart2["country"] = data_chart2["country"].astype(str)
            data_chart2.reset_index(drop=True)


            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable3)+"' & type_horizon=='"+str(time_ref)+"'")
            data_chart3 = list_matrix1.query(str(search_query))
            data_chart3=data_chart3[['country','type_horizon','coefficient','t_statistic']]
            data_chart3["coefficient"] = pd.to_numeric(data_chart3["coefficient"])
            data_chart3["t_statistic"] = pd.to_numeric(data_chart3["t_statistic"])
            data_chart3["country"] = data_chart3["country"].astype(str)
            data_chart3["country1"] = data_chart3["country"]
            data_chart3["country1"] = data_chart3["country1"].astype('category')
            data_chart3 = data_chart3.copy()
            data_chart3.drop_duplicates()
            print(data_chart3)
            data_chart3.drop_duplicates()
            data_chart3["country"] = data_chart3["country"].astype(str)
            data_chart3.reset_index(drop=True)

            
            
            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable4)+"' & type_horizon=='"+str(time_ref)+"'")
            data_chart4 = list_matrix1.query(str(search_query))
            data_chart4=data_chart4[['country','type_horizon','coefficient','t_statistic']]
            data_chart4["coefficient"] = pd.to_numeric(data_chart4["coefficient"])
            data_chart4["t_statistic"] = pd.to_numeric(data_chart4["t_statistic"])
            data_chart4["country"] = data_chart4["country"].astype(str)
            data_chart4["country1"] = data_chart4["country"]
            data_chart4["country1"] = data_chart4["country1"].astype('category')
            data_chart4 = data_chart4.copy()
            data_chart4.drop_duplicates()
            print(data_chart4)
            data_chart4.drop_duplicates()
            data_chart4["country"] = data_chart4["country"].astype(str)
            data_chart4.reset_index(drop=True)
            
            
            search_query = ("variable_x=='"+str(x_variable)+"' & type_variable_y =='"+str(y_variable5)+"' & type_horizon=='"+str(time_ref)+"'")
            data_chart5 = list_matrix1.query(str(search_query))
            data_chart5=data_chart5[['country','type_horizon','coefficient','t_statistic']]
            data_chart5["coefficient"] = pd.to_numeric(data_chart5["coefficient"])
            data_chart5["t_statistic"] = pd.to_numeric(data_chart5["t_statistic"])
            data_chart5["country"] = data_chart5["country"].astype(str)
            data_chart5["country1"] = data_chart5["country"]
            data_chart5["country1"] = data_chart5["country1"].astype('category')
            data_chart5 = data_chart5.copy()
            data_chart5.drop_duplicates()
            print(data_chart5)
            data_chart5.drop_duplicates()
            data_chart5["country"] = data_chart5["country"].astype(str)
            data_chart5.reset_index(drop=True)
            
            
            
            
            print(n)
            n=n+1
            print("----------------")

            df1 = data_chart1
            df2 = data_chart2
            df3 = data_chart3
            df4 = data_chart4
            df5 = data_chart5
            
            
            del data_chart1
            del data_chart2
            del data_chart3
            del data_chart4
            del data_chart5

            # Data
            x1 = df1["coefficient"]
            y1 = df1["t_statistic"]
            x2 = df2["coefficient"]
            y2 = df2["t_statistic"]
            x3 = df3["coefficient"]
            y3 = df3["t_statistic"]
            x4 = df4["coefficient"]
            y4 = df4["t_statistic"]
            x5 = df5["coefficient"]
            y5 = df5["t_statistic"]
            
            labels1 = df1["country1"]
            labels2 = df2["country1"]
            labels3 = df3["country1"]
            labels4 = df4["country1"]
            labels5 = df5["country1"]
    
            print("----------------")
            # Create the figure and axes objects
            #fig, ax = plt.subplots(1, figsize=(10, 6))
            #del fig
            #del ax
            fig, ax = plt.figure(figsize=(20,20))
            #fig, ax = plt.figure(figsize=(parameter_s1,parameter_s2))
            #plt.figure(figsize=((10,8)))
            #fig.suptitle("EM Global Macro Sensitivity Analysis: "+str(x_variable)+" vs. EM ["+str(time_ref_name)+"]",size = 15)
            plt.title('Interpretation: t-stat ->  significance // reg coefficient -> sensitivity ', size=parameter_l)
            plt.ylabel(y_label, size=parameter_l)
            plt.xlabel(x_label, size=parameter_l)

            # Plot the scatter points
            ax.scatter(x1, y1,color="blue",s=100,alpha=0.5, linewidths=1,label=("Blue: ["+str(y_variable1)+"]"))  # Size of edge around the dots
            ax.scatter(x2, y2,color="red",s=100,alpha=0.5, linewidths=1,label=("Red: ["+str(y_variable2)+"]"))
            ax.scatter(x3, y3,color="green",s=100,alpha=0.5, linewidths=1,label=("Green: ["+str(y_variable3)+"]"))
            ax.scatter(x4, y4,color="orange",s=100,alpha=0.5, linewidths=1,label=("orange: ["+str(y_variable4)+"]"))
            ax.scatter(x5, y5,color="purple",s=100,alpha=0.5, linewidths=1,label=("purple: ["+str(y_variable5)+"]"))

            # Add the participant names as text labels for each point
            for x1_pos, y1_pos, label1 in zip(x1, y1, labels1):
                    ax.annotate(label1,             # The label for this point
                                xy=(x1_pos, y1_pos), # Position of the corresponding point
                                xytext=(7, 0),     # Offset text by 7 points to the right
                                textcoords='offset points', # tell it to use offset points
                                ha='left',         # Horizontally aligned to the left
                                va='center')       # Vertical alignment is centered

            for x2_pos, y2_pos, label2 in zip(x2, y2, labels2):
                    ax.annotate(label2,             # The label for this point
                                xy=(x2_pos, y2_pos), # Position of the corresponding point
                                xytext=(7, 0),     # Offset text by 7 points to the right
                                textcoords='offset points', # tell it to use offset points
                                ha='left',         # Horizontally aligned to the left
                                va='center') 

            for x3_pos, y3_pos, label3 in zip(x3, y3, labels3):
                    ax.annotate(label3,             # The label for this point
                                xy=(x3_pos, y3_pos), # Position of the corresponding point
                                xytext=(7, 0),     # Offset text by 7 points to the right
                                textcoords='offset points', # tell it to use offset points
                                ha='left',         # Horizontally aligned to the left
                                va='center') 
                    
            for x4_pos, y4_pos, label4 in zip(x4, y4, labels4):
                    ax.annotate(label4,             # The label for this point
                                xy=(x4_pos, y4_pos), # Position of the corresponding point
                                xytext=(7, 0),     # Offset text by 7 points to the right
                                textcoords='offset points', # tell it to use offset points
                                ha='left',         # Horizontally aligned to the left
                                va='center') 
                    
                    
            for x5_pos, y5_pos, label5 in zip(x5, y5, labels5):
                    ax.annotate(label5,             # The label for this point
                                xy=(x5_pos, y5_pos), # Position of the corresponding point
                                xytext=(7, 0),     # Offset text by 7 points to the right
                                textcoords='offset points', # tell it to use offset points
                                ha='left',         # Horizontally aligned to the left
                                va='center')         
                    

            ax.legend(loc="lower right",title="EM Variables")    
            plt.grid()
            sns.set_style('whitegrid')
            ax.axhline(0, color='black', lw=1, alpha=0.75)
            ax.axvline(0, color='black', lw=1, alpha=0.75)
            # Show the plot
            n1=str(n)
            n1=n1.rjust(5, '0')
            plt.savefig(("pdf_y_comp/GM_agg_comp"+str(n1)+"x_"+str(x_variable)+"_th"+str(time_ref)+".pdf"), bbox_inches='tight')
            plt.close()
            plt.close('all')
            plt.clf()
            plt.cla()
            del fig
            del ax
print("Complete!!!!")

    
print("Complete!!")        
t1 = time.time()
total = t1-t0
print("timer: "+str(total)+" seconds")   


now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


#TypeError: cannot unpack non-iterable Figure object

#<Figure size 1224x864 with 0 Axes>

del fig
del ax


# In[ ]:


source_dir= 'K:/2020_2431/q/gm_sensitivity/images/pdf_y_comp/'
source_dir2= 'K:/2020_2431/q/gm_sensitivity/images/pdf_y_comp/Agg/Comparison_'
 
    
#####filter time set here
merger = PdfFileMerger()
for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(source_dir + item)

merger.write(source_dir2+"Graph_Complete.pdf") 
merger.close()



now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


data_z = pd.read_csv (r'K:\2020_2431\q\sandbox_gm\data_z.csv')


# In[ ]:


#######

os.chdir('K:/2020_2431/q/gm_sensitivity/images/')
print(os.getcwd())

Previous_Date = datetime.today() - timedelta(days=1)
Previous_Date=Previous_Date.strftime('%Y-%m-%d')
time_ref_start_n=datetime.today() - relativedelta(months=12) 
time_ref_start_n=time_ref_start_n.strftime('%Y-%m-%d')
time_ref_end_n=Previous_Date
time_ref_name=str(time_ref_start_n)+" / "+str(time_ref_end_n)
    
loop_data = data_z[(data_z['date'] > str(time_ref_start_n)) & (data_z['date'] < str(time_ref_end_n))]
x_list=['dv_ust10y','dv_msci_us','dv_vix', 'dv_brent_oil_act','dv_gold',]
y_list=['dv_cds5y_','dv_fx_','dv_l_msci_']
country_list = ['BRL','COP','MXN','CLP','PEN','CZK','HUF','PLN','RUB','ILS','ZAR','TRY','IDR','THB','MYR','KRW']
#PHP
parameter_s1=10
parameter_s2=10
parameter_l=15
##exog
x_label="x label"
##endog
y_label="y label"
n=1

for x in range(len(x_list)): 
    x_variable=str(x_list[x])
    loop_data_x=loop_data[[str(x_variable)]]


    for y in range(len(y_list)):          
        y_variable=str(y_list[y])
        filter_col = [col for col in data_z if col.startswith(str(y_variable))]
        loop_data_y=loop_data[filter_col] 
        
        for z in range(len(country_list)): 
                country_name=str(country_list[z])
                column_country=loop_data_y.filter(like=str(country_name)).columns
                loop_data_y1=loop_data_y[column_country]           
                endog=loop_data_y1
                exog=loop_data_x
                x_label=str(x_variable)
                y_label=str(y_variable)
                # Create the figure and axes objects
                
                fig, ax = plt.subplots(1, figsize=(10, 6))
                ax.scatter(exog, endog ,color="blue",s=90,alpha=0.5, linewidths=1,label=("Blue: ["+str(y_variable)+"]"))  # Size of edge around the dots
                
                plt.ylabel(y_label, size=parameter_l)
                plt.xlabel(x_label, size=parameter_l)
                sns.set_style('whitegrid')
                
                
                
                
                
                data_trend = pd.concat([exog, endog], axis=1)
                #print(data_trend)
                sns.lmplot(x=str(exog.columns[0]), y=str(endog.columns[0]), data=data_trend);
                ax.axhline(0, color='black', lw=1, alpha=0.75)
                ax.axvline(0, color='black', lw=1, alpha=0.75)    
                fig.suptitle("EM Global Macro Sensitivity Analysis: "+str(x_variable)+" vs."+str(country_name)+" "+str(y_variable) +"["+str(time_ref_name)+"]",size = 15)
                plt.title("EM Global Macro Sensitivity Analysis: "+str(x_variable)+" vs."+str(country_name)+" "+str(y_variable)+"["+str(time_ref_name)+"]", size=10) 
                
                n1=str(n)
                n1=n1.rjust(5, '0')
                plt.savefig(("pdf_scatter/GM_agg_"+str(n1)+"x_"+str(x_variable)+"_y_"+str(y_variable)+"_c_"+str(country_name)+".pdf"), bbox_inches='tight')
                #plt.show()
                plt.close()
                plt.close('all')
                plt.clf()
                plt.cla()
                
                del data_trend
                del endog
                del exog
                del loop_data_y1
                
                
                n=n+1
                print(n)
                

print("Complete!!")        

now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)



# In[ ]:


source_dir= 'K:/2020_2431/q/gm_sensitivity/images/pdf_scatter/'
source_dir2= 'K:/2020_2431/q/gm_sensitivity/images/pdf_scatter/Agg/'
 
    
#####filter time set here
merger = PdfFileMerger()
for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(source_dir + item)

merger.write(source_dir2+"Scatter_Graph_Complete.pdf") 
merger.close()

print("COmplete!!")

now = datetime.now()
print("Y",now.year,"/ M", now.month,"/ D", now.day, "/// H",now.hour,": M", now.minute,": S", now.second)


# In[ ]:


#Copy paste

####suamrry tables
import subprocess


src=r'K:\2020_2431\q\gm_sensitivity\images\table\Summary\dv_cds5y__Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_cds5y__Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\table\Summary\dv_fx__Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_fx__Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\table\Summary\dv_l_msci__Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_l_msci__Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\table\Summary\dv_hccy__Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_hccy__Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)  

src=r'K:\2020_2431\q\gm_sensitivity\images\table\Summary\dv_lccy__Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_lccy__Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)
###################################################
    
    
src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_brent_oil_act_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_brent_oil_act_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_copper_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_copper_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_corp_spread_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_corp_spread_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_dax_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_dax_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ftse_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ftse_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_gold_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_gold_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_msci_us_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_msci_us_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_silver_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_silver_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ted_spread_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ted_spread_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ust2y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ust2y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ust3m_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ust3m_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ust5y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ust5y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ust7y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ust7y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_ust10y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_ust10y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_x_dv\x_dv_vix_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\x_dv_vix_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

################################################################################################
 
src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_y_comp\Agg\Comparison_Graph_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\Comparison_Graph_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)    

    
####################################################

src=r'K:\2020_2431\q\gm_sensitivity\images\pdf_scatter\Agg\Scatter_Graph_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\Scatter_Graph_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

##################################################################################################



###correlation
src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_copper_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_copper_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_corp_spread_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_corp_spread_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)



src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_dax_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_dax_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ftse_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ftse_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_gold_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_gold_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_msci_us_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_msci_us_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)



src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_silver_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_silver_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)



src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ted_spread_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ted_spread_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_gold_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_gold_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)



src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ust3m_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ust3m_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ust2y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ust2y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ust5y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ust5y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)

src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ust7y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ust7y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_ust10y_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_ust10y_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)


src=r'K:\2020_2431\q\gm_sensitivity\images\correlation\pdf_x_dv\dv_vix_Complete.pdf'
dst=r'P:\Technology\AlphaQuant\pdf_render_svc_files\AlanM\gm_sen\dv_vix_Complete.pdf'  
cmd='copy "%s" "%s"' % (src, dst)
status = subprocess.call(cmd, shell=True)



# In[ ]:


#print(exog)
#print(endog)
#data_trend = pd.concat([exog, endog], axis=1)
#print(data_trend)
#sns.lmplot(x=str(x_variable), y=str(y_variable), data=data_trend);
#exog = exog.values.flatten()
#endog = endog.values.flatten()           
#z= polyfit(exog, endog, 1)
#p= np.poly1d(z)
#plt.plot(exog,p(exog),"r--")


# In[ ]:


###### clear output and then save
import os
def clear():
    os.system( 'cls' )


clear()



# In[ ]:


print("COmpelte")

