import pandas as pd

# DataFrame

# df = pd.DataFrame(
#     {
#         "Name": [
#             "Braund, Mr. Owen Harris",
#             "Allen, Mr. William Henry",
#             "Bonnell, Miss. Elizabeth",
#         ],
#         "Age": [22, 35, 58],
#         "Sex": ["male", "male", "female"],
#         "Address" : ["London","Toronto","Paris"],
#         "Country" : ["UK","Canada","France"]

#     }
# )

# print(df)
# print(df["Sex"])
# print(df["Age"].max())
# x = df.describe()
# print(x)


# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

#load data into a DataFrame object:
# df = pd.DataFrame(data)
# print(df)

# Locate Row
# print(df.loc[1])
# print(df.loc[[0, 1, 2]])

# Named Indexes
# df = pd.DataFrame(data, index = ["day1","day2","day3"])
# print(df)
# print()
#refer to the named index:
# print(df.loc["day2"])

# Load Files Into a DataFrame
# df = pd.read_csv('data.csv')

# print(df)
# print()
# print(df.loc[[5,6,7]])
# print(df.head(20))
# print()
# print(df.tail(20))
# print()
# print(df.describe())

# df.to_excel("data.xlsx", sheet_name="Nutrition", index=False)

# print(df.info())

# cal = df["Calories"]
# print(cal)
# print("it prints type:",type(cal))

# print(cal.head(11))

# y = len(df["Calories"])
# print(y)

data = {
    'Name': ['John', 'Alice', 'Bob', 'Emily'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the file path where you want to save the Excel file
file_path = 'data.xlsx'

# Export the DataFrame to an Excel file
df.to_excel(file_path, index=False)

print("Excel file exported successfully!")