print('Import moduls')

import pandas as pd
import tkinter as tk
from tkinter import filedialog
import re

print('Import successful')

# Create a root window (it will be hidden)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open file dialog and get the filename
file_path1 = filedialog.askopenfilename(
    title="Select base file",
    filetypes=[("Excel", "*.xlsx")],
)


# Create a root window (it will be hidden)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open file dialog and get the filename
file_path2 = filedialog.askopenfilename(
    title="Select base file",
    filetypes=[("Excel", "*.xlsx")],
)

# Create a root window (it will be hidden)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open directory dialog and get the folder path
folder_path = filedialog.askdirectory(
    title="Select save folder"
)


print("Importing files")
xlsx1 = pd.read_excel(file_path1, sheet_name="Energiedaten")
xlsx2 = pd.read_excel(file_path2, sheet_name="Energiedaten")
print('Import successful')

tmp1 = xlsx1
tmp2 = xlsx2

# Define the pattern
pattern = r'AT\d{32}'

# Function to check if a column name matches the pattern
def matches_pattern(column_name):
    return bool(re.match(pattern, column_name))

# Iterate through columns in tmp2 and add matching ones to tmp1
for col in tmp2.columns:
    if matches_pattern(col) and col in tmp1.columns:
        # Keep original values for rows 0-14
        # No conversion needed here as we're keeping original values
        
        # Add values from row 15 onwards
        # Convert to float only for the addition operation
        min_length = min(len(tmp1.index[15:]), len(tmp2.index[15:]))
        
        tmp1.iloc[15:15+min_length, tmp1.columns.get_loc(col)] = (
            tmp1.iloc[15:15+min_length, tmp1.columns.get_loc(col)].astype(float).values +
            tmp2.iloc[15:15+min_length, tmp2.columns.get_loc(col)].astype(float).values
        )

print("Exporting File")
tmp1.to_excel(folder_path+'/output.xlsx', sheet_name='Energiedaten' ,index=False)