# Pandas - Cleaning Data
"""
    1.Data Cleaning
        Data cleaning means fixing bad data in your data set.

        Bad data could be:
        
        Empty cells
        Data in wrong format
        Wrong data
        Duplicates
        
"""


# Pandas - Cleaning Empty Cells

import pandas as pd

df = pd.read_csv('data.csv')
 
# new_df = df.dropna()

# change the original DataFrame, use the inplace = True
# new_df = df.dropna(inplace=True)

# print(new_df.to_string())

# df.dropna(inplace=True)

# try:
#     df.to_excel("dataass.xlsx", index=True)
#     print("Excel file exported successfully!")
# except Exception as e:
#     print("Error exporting Excel file:", e)

# Replace Empty Values

# df.fillna(130, inplace = True)
# try:
#     df.to_excel("dataass.xlsx", index=True)
#     print("Excel file exported successfully!")
# except Exception as e:
#     print("Error exporting Excel file:", e)

# Replace Only For Specified Columns

# df["Calories"].fillna(130, inplace = True)

# df.fillna({
#     "Calories": 130
# }, inplace= True)

# try:
#     df.to_excel("dataass.xlsx", index=True)
#     print("Excel file exported successfully!")
# except Exception as e:
#     print("Error exporting Excel file:", e)


# Replace Using Mean, Median, or Mode

# x = df["Calories"].mean()
# # x = df["Calories"].median()
# # x = df["Calories"].mode()

# df["Calories"].fillna(x, inplace = True)

# try:
#     df.to_excel("dataasss.xlsx", index=True)
#     print("Excel file exported successfully!")
# except Exception as e:
#     print("Error exporting Excel file:", e)

# df.loc[7, 'Duration'] = 45
# print(df.to_string())

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
    
# print(df)
# print(df.loc[7])
# print(df.head(10))

# Removing Duplicates
# x = df.duplicated()
# print(x.to_string())

# df.drop_duplicates(inplace=True)
# print(df.to_string())

print(df.corr())
