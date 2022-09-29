import numpy as np

def get_column(table, header, col_name):
    col = []
    col_index = header.index(col_name)
    for row in table:
        col.append(row[col_index])

    return col

def get_frequencies(table, header, col_name):
    col = get_column(table, header, col_name)
    col.sort() # inplace sort

    values = [] # 75, 76, 77
    counts = [] # 2, 1, 1
    for value in col:
        if value not in values:
            # first time seeing this value
            values.append(value)
            counts.append(1)
        else:
            # seen this value before
            counts[-1] += 1 # ok because the list is in sorted order
    return values, counts

def dummy_function():
    print("Hello!!! AGAIN ~~~~dijfaksjf")

def group_by(table, header, group_by_col_name):
    group_by_col = get_column(table, header, group_by_col_name)
    group_by_col_index = header.index(group_by_col_name)

    group_names = sorted(list(set(group_by_col))) # e.g. [75, 76, 77]
    group_subtables = [[] for _ in group_names] # e.g. [[], [], []]

    