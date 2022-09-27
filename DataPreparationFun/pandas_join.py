import pandas as pd 
# pandas is short for panel data
# it is a library, like numpy, for data science
# it is built on numpy

# one of the major shortcomings of using lists
# for data science, is the lack of label-based indexing
# e.g. the header!!
# also really great builtin functionality for indexing, cleaning,
# stats, etc....

# there are two main objects in pandas
# 1D data: pandas Series
# 2D data: pandas DataFrame (every column is a series)

# now, join demo with pandas' DataFrames!!

# first trace example (single key)
# adapted from SQL examples at https://www.diffen.com/difference/Inner_Join_vs_Outer_Join
header_left = ["Product", "Price"]
data_left = [["Potatoes", 3.0],
                ["Avacodos", 4.0],
                ["Kiwis", 2.0],
                ["Onions", 1.0],
                ["Melons", 5.0],
                ["Oranges", 5.0],
                ["Tomatoes", 6.0]]
header_right = ["Product", "Quantity"]
data_right = [["Potatoes", 45.0],
                ["Avacodos", 63.0],
                ["Kiwis", 19.0],
                ["Onions", 20.0],
                ["Melons", 66.0],
                ["Broccoli", 27.0],
                ["Squash", 92.0]]

# pandas dataframe demo
df_left = pd.DataFrame(data_left, columns=header_left)
df_right = pd.DataFrame(data_right, columns=header_right)

# inner join
df_inner_joined = df_left.merge(df_right, how="inner", on=["Product"])
print("Inner Join:")
print(df_inner_joined)
print()

# outer join
df_outer_joined = df_left.merge(df_right, how="outer", on=["Product"])
print("Outer Join:")
print(df_outer_joined)
print()