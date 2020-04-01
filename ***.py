import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

os.chdir("/Users/jiwoonhwang/Desktop/MBTS")
path=("/Users/jiwoonhwang/Desktop/MBTS/pooled_pos_con_sub_BLANK.xlsx")
order_of_run=pd.read_excel(path, sheet_name="Sheet1")
path=("/Users/jiwoonhwang/Desktop/MBTS/order_of_run_actual.xlsx")
std=pd.read_excel(path, sheet_name="sheet")

standard=pd.DataFrame()

for col in order_of_run.columns:
	standard[col]=std[col]

writer = pd.ExcelWriter('pooled_pos_con_sub_BLANK.xlsx', engine='openpyxl')
if os.path.exists('pooled_pos_con_sub_BLANK.xlsx'):
	book = load_workbook('pooled_pos_con_sub_BLANK.xlsx')
	writer.book = book

#fill zeroes
#df2=df2.fillna('NA')

#create new sheet
standard.to_excel(writer, sheet_name='weirdTAGs_standard')
writer.save()
writer.close()

