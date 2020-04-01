import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/waxester.xlsx"
df =pd.read_excel(path, sheet_name='DAG_standard')
df2=pd.read_excel(path, sheet_name='WaxEster')

#find highest value
value=df.max(axis=1)
print "This is the highest value: " +str(value)
# value=1
# for col in range(df.shape[1]):
# 	new_value=df.iat[0,col]
# 	if new_value>value:
# 		value=new_value
# 		#print value
# 	else:
# 		continue
#print "This is the final value:" + str(value) 

#calculate normalizing factor
df1= df.apply(lambda row: row/float(value), axis=1)
factor= df1.iloc[0,:]
print factor

#apply factor to all rows
df2=df2.apply(lambda row: row/factor, axis=1)

#load workbook to save new dataframe in
writer = pd.ExcelWriter('waxester.xlsx', engine='openpyxl')
if os.path.exists('waxester.xlsx'):
	book = load_workbook('waxester.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet, save new dataframe
df2.to_excel(writer, sheet_name='WaxEster_norm')
writer.save()
writer.close()
#print df.mul(1/float(value), axis=1).head
 
#print float(df.max(axis=1))