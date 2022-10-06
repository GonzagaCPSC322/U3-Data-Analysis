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

    # walk through each row and figure out which subtable 
    # it belongs to
    for row in table:
        group_by_val = row[group_by_col_index]
        subtable_index = group_names.index(group_by_val) # e.g. 0 1 or 2
        group_subtables[subtable_index].append(row)
    return group_names, group_subtables

def compute_equal_width_cutoffs(values, num_bins):
    values_range = max(values) - min(values)
    bin_width = values_range / num_bins
    # bin_width is probably a float
    # we will use numpy's version of range()
    cutoffs = list(np.arange(min(values), max(values), bin_width))
    cutoffs.append(max(values))
    # optionally, round
    cutoffs = [round(cutoff, 2) for cutoff in cutoffs]
    return cutoffs

def compute_bin_frequencies(values, cutoffs):
    freqs = [0 for _ in range(len(cutoffs) - 1)] # because N + 1 cutoffs

    for value in values:
        if value == max(values):
            freqs[-1] += 1 # add one to the last bin count
        else:
            for i in range(len(cutoffs) - 1):
                if cutoffs[i] <= value < cutoffs[i + 1]:
                    freqs[i] += 1 
                    # add one to this bin defined by [cutoffs[i], cutoffs[i+1])
    return freqs

def compute_slope_intercept(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)
    
    m = sum([(x[i] - meanx) * (y[i] - meany) for i in range(len(x))]) / \
        sum([(x[i] - meanx) ** 2 for i in range(len(x))])

    # y = mx + b => b = y - mx
    b = meany - m * meanx
    return m, b