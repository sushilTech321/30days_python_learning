import pandas as pd

# Pandas Read CSV

df = pd.read_csv('data.csv')

# use to_string() to print the entire DataFrame.
# print(df.to_string()) 

# Pandas will only return the first 5 rows, and the last 5 rows
# print(df)

# max_rows
# print(pd.options.display.max_rows) 

# pd.options.display.max_rows = 9999

# df = pd.read_csv('data.csv')

# print(df) 



# Read JSON

df = pd.read_json('data.json')
# print(df)
# print(df.to_string())

# Dictionary as JSON
# data = {
#     "Duration": {
#         "0": 60,
#         "1": 60,
#         "2": 60,
#         "3": 45,
#         "4": 45,
#         "5": 60,
#     },

#     "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
    
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
  
#    "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)
# print(df)


# Analyzing DataFrames
# x = df.head(10)
# y = df.tail(10)
# z = df.info()
# print(z)