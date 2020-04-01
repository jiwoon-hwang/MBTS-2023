import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math
import glob

os.chdir("/Users/jiwoonhwang/Desktop/MBTS/metaboanalyst")
path=("/Users/jiwoonhwang/Desktop/MBTS/Pooled_pos_all_norm_withNA_edit.csv")
template=pd.read_csv(path)

dups= template[template['compound_name'].duplicated(keep=False)]
dups=dups[dups['compound_name'].notnull()]

# print template['compound_name'].duplicated(keep=False)

print dups

dups.loc[:,'compound_name']=dups.loc[:,'compound_name']+ "_RT:"

print type(dups.loc[:,'compound_name'])
dups.loc[:,'compound_name'].values=dups.loc[:,'compound_name'].values+dups.loc[:,'peakgroup_rt'].values

print dups

# template.drop_duplicates('compound_name', keep=False, inplace=True)
# template=template.append(dups)
# template=template.sort_index()

# nan=template[template['compound_name'].isna()]
# nan['compound_name']=nan['compound_name'].fillna("NA_")

# c=nan.groupby("compound_name").cumcount()
# c=(c+1).astype(str)
# nan['compound_name']+=c
# template[template['compound_name'].isna()]=nan


# print template.iloc[520:530]


# c=template.groupby('compound_name').cumcount()
# c=c.replace(0,'').astype(str)
# c=c.replace(1,'')
# template['compound_name']=template['compound_name']+" "+c

# template.to_csv('Pooled_pos_all_norm_wtihNA_no_duplicates.csv', index=False)