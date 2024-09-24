


def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table:
        col.append(row[col_index])

    return col

def dummy_function():
    print("hello from dummy function (again!!)")