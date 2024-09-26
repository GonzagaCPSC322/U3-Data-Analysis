


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