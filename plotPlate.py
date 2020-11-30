# 0. Set up packages we need

# Import everything:
import numpy as np # Maths functions, matrices 
import matplotlib.pyplot as plt # Plotting
import pandas as pd # Dataframes, which are more advanced arrays, useful for storing and manipulating data

# Parameters which must be set before running code
OUTPUT_FILE = './reduced_data/reduced_data.xlsx'
OUTPUT_PLOT = './reduced_data/plot.pdf'

# 1. Read file
xls = pd.ExcelFile(OUTPUT_FILE)
# 2. Select sheet and put into dataframe
df = pd.read_excel(xls,sheet_name='Sheet 0')

# Plot and save
df = pd.read_excel(xls,sheet_name='Sheet 0')
plt.plot(df['Time (s)']/3600, df['F09']);
plt.xlabel("Time (h)"); plt.ylabel("485/520 gain=800"); 
plt.savefig(OUTPUT_PLOT, format='pdf') 
