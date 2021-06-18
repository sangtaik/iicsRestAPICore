import numpy as np
import pandas as pd
import json
import sys
import os
from openpyxl import Workbook


base_dir = "C:/Users/admin/Documents/data"
file_nm = "df.xlsx"
xlxs_dir = os.path.join(base_dir, file_nm) 

def exportExcelFile(data):
    df = pd.DataFrame(data)
    df.to_excel("output.xlsx")
 