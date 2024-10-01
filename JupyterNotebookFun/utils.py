import numpy as np


def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table:
        col.append(row[col_index])

    return col

def dummy_function():
    print("hello from dummy function (again!!)")

def get_frequencies(table, header, col_name):
    # TODO: resolve this using python dictionaries
    col = get_column(table, header, col_name)
    # we want to get the unique values from this column
    unique_col_values = sorted(list(set(col)))
    print(unique_col_values)
    counts = []
    for val in unique_col_values:
        counts.append(col.count(val))

    return unique_col_values, counts

def group_by(table, header, group_by_col_name):
    col = get_column(table, header, group_by_col_name)
    unique_col_values = sorted(list(set(col)))
    group_by_col_index = header.index(group_by_col_name)
    group_subtables = [[] for _ in unique_col_values]

    for row in table:
        group_by_val = row[group_by_col_index]
        subtable_index = unique_col_values.index(group_by_val)
        group_subtables[subtable_index].append(row)

    return unique_col_values, group_subtables

def compute_equal_width_cutoffs(values, num_bins):
    values_range = max(values) - min(values)
    bin_width = values_range / num_bins
    # bin_width is probably a float
    # we will use numpy's version of range()
    # https://numpy.org/doc/stable/reference/generated/numpy.arange.html
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
    meanx = sum(x) / len(x)
    meany = sum(y) / len(y)

    num = sum([(x[i] - meanx) * (y[i] - meany) for i in range(len(x))])
    den = sum([(x[i] - meanx) ** 2 for i in range(len(x))])
    m = num / den
    # y = mx + b -> y - mx
    b = meany - m * meanx
    return m, b