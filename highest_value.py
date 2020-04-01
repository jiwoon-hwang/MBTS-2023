import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math


#change directory
os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path ="/Users/jiwoonhwang/Desktop/MBTS/pooled_pos_con.xlsx"
df =pd.read_excel(path, sheet_name='DAG_standard')

value=1
for col in range(df.shape[1]):
	new_value=df.iat[0,col]
	if new_value>value:
		value=new_value
		#print value
	else:
		continue
print "This is the final value:" + str(value)


# writer = pd.ExcelWriter('pooled_pos_con.xlsx', engine='openpyxl')
# if os.path.exists('pooled_pos_con.xlsx'):
# 	book = load_workbook('pooled_pos_con.xlsx')
# 	writer.book = book

# #fill zeroes
# #df2=df2.fillna('NA')

# #create new sheet
# df2.to_excel(writer, sheet_name='IP_DAG_norm')
# writer.save()
# writer.close()
# #print df.mul(1/float(value), axis=1).head
 
# #print float(df.max(axis=1))