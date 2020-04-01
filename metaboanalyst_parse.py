import os
import pandas as pd
import openpyxl
import xlrd
import numpy as np
from openpyxl import load_workbook
import math

os.chdir('/Users/jiwoonhwang/Desktop/MBTS/')
path = '/Users/jiwoonhwang/Desktop/MBTS/Pooled_pos_all_norm_withNA.csv'
all_norm=pd.read_csv(path, low_memory=False)

wax_esters=all_norm[all_norm['species']=="WaxEster"]
pigment = all_norm[all]