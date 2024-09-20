import numpy as np

def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table:
        col.append(row[col_index])

    return col

def main():
    msrp_header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", 75, 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789]]
    
    msrps = get_column(msrp_table, msrp_header, "MSRP")
    print(msrps)

    # more on attributes
    # 1. what is the attribute's type?
    # e.g. how is it stored?
    # int, float, str, etc.
    # 2. what is the attribute's semantic type?
    # e.g. what does it represent? --> domain knowledge
    # 3. what is its measurement scale?
    # e.g. categorical vs continuous (numeric)

    # noisy vs invalid values
    # noisy: valid on the scale, but recorded incorrectly
    # ex: age attribute
    # a 18 year old who incorrectly enters 81 years of age
    # invalid: not valid on the scale
    # ex: enters "bob" for age

    # missing values
    # 2 main ways to deal
    # 1. discard them
    # generally, we do not want to throw data away
    # generally okay when our dataset is large and our missing values are rare
    # 2. fill them
    # generally fill with central tendency measures
    # 2.A. numeric: median, mean, mid value, etc.
    # 2.B. categorical: mode (most frequent value, perhaps based on a subset)
    # OR more sophisticated methods... like kNN to fill the missing values

    # quick notes on summary stats (+ some more python)
    # central tendency measures: measure the "middle" values of a dataset/attribute
    # mean is impacted grealty by outliers, sometimes prefer median instead
    # mid value: (min + max) / 2
    # data dispersion: measure the spread of data
    # variance, stdev, quantiles/percentiles, etc.
    # variance is the mean of the squared mean deviations
    # lets calculate for msrps
    msrp_mean = sum(msrps) / len(msrps)
    msrp_squared_deviations = [(msrp - msrp_mean) ** 2 for msrp in msrps]
    print(msrp_squared_deviations)
    msrp_var = sum(msrp_squared_deviations) / len(msrp_squared_deviations)
    msrp_std = msrp_var ** 0.5
    print(msrp_std)
    # lets compare our std calc with numpy's
    # assert msrp_std == np.std(msrps)
    # best practice when comparing floats is to use np.isclose()
    # or np.allclose() for sequences of floats
    # https://numpy.org/doc/stable/reference/generated/numpy.isclose.html
    assert np.isclose(msrp_std, np.std(msrps))

# python main.py --> __name__ stores "__main__"
if __name__ == "__main__":
    main()