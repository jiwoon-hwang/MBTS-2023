import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

path= '/Users/jiwoonhwang/Desktop/MBTS/Pooled_pos_all_norm_withNA_edit.csv'
df=pd.read_csv(path)

nan=df[df['compound_name'].isna()]

# print nan

# count=0
# for i in nan.index:
# 	count+=1
# 	nan.loc[i,'compound_name']="NA_"+str(count)
nan['compound_name']=nan['compound_name'].fillna("NA_")

c=nan.groupby("compound_name").cumcount()
c=(c+1).astype(str)
# print c

nan['compound_name']+=c



# print (nan)
# print (len(nan['compound_name']))

# for i in range(len(nan['compound_name'])):
#     nan.loc[i,1]="NA_"+str(i)

# nan.loc[0]

df[df['compound_name'].isna()]=nan
print df.iloc[520:530]